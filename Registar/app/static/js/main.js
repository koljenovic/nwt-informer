var app = angular.module('kontakt', ['ngRoute', 'ngResource', 'djng.forms', 'pascalprecht.translate', 'ui.bootstrap', 'ngCookies', 'ngAnimate', 'ngFileUpload']);
app.config(function ($interpolateProvider, $translateProvider, $resourceProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{-');
    $interpolateProvider.endSymbol('-}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $translateProvider.translations('en', {
        home: 'Home',
        about: 'About',
        contact: 'Contact',
    });
    $translateProvider.translations('bs', {
        home: 'Početna',
        about: 'O aplikaciji',
        contact: 'Kontakt',
    });
    $translateProvider.preferredLanguage('en');
});
app.factory('User', ['$resource', function($resource) {
    return $resource('/api/user/:id/',
        {id: '@id'},
        {
            'query' : {'method': 'GET', isArray: false}
        });
}]);
app.factory('Osoba', ['$resource', function($resource) {
    return $resource('/api/osoba/:id/',
        {id: '@id'},
        {
            'query' : {'method': 'GET', isArray: false},
            'update': {'method': 'PUT'}
        });
}]);
app.factory('Firma', ['$resource', function($resource) {
    return $resource('/api/firma/:id/',
        {id: '@id'},
        {
            'query' : {'method': 'GET', isArray: false},
            'update': {'method': 'PUT'}
        });
}]);
app.factory('Grad', ['$resource', function($resource) {
    return $resource('/api/grad/:id/',
        {id: '@id'},
        {'query' : {'method': 'GET', isArray: false}});
}]);
app.controller('SearchCtrl', function ($scope, $http) {
    $scope.legalese = false;
    $scope.firmaSearch = function (searchString, page=1) {
        $scope.currentPage = page;
        $scope.firmaSearchString = searchString;
        return $http.get('/search/', { params: { 'text__startswith': searchString, 'page': page }})
            .then(function(response) {
                $scope.searchData = response.data;
        });
    }
    $scope.loadPage = function () {
        $scope.firmaSearch($scope.firmaSearchString, $scope.currentPage);
    }
});
app.controller('PageCtrl', function ($scope, $http, $routeParams, $location, $timeout, Upload, Firma, Grad) {
    $.ajax({
        url: '/api/kontakt/',
        method: 'GET'
    }).then(function(data) {
        $scope.dummy = data.results;
        $scope.$apply(function() {
            $scope.dummy.push(data.results);
            $scope.quantity = $scope.dummy.length - 1;

            $scope.kontakti = [];
            $scope.kategorije = [];
            for (var i=0; i<$scope.quantity; i++) {
                if ($scope.dummy[i].firma_fk == $routeParams['firmaId']) {
                    $scope.kontakti.push($scope.dummy[i]);
                    if($scope.kategorije.indexOf($scope.dummy[i].naziv) == -1)
                        $scope.kategorije.push($scope.dummy[i].naziv);
                }
            }

        });
    });
    $scope.search = function (searchString, slice_size=0) {
        return $http.get('/search/', { params: { 'text__startswith': searchString }})
            .then(function(response) {
                if (slice_size > 0) {
                    return response.data.results.slice(0, slice_size);
                } else {
                    return response.data;
                }
        });
    }
    $scope.searchSelect = function (item, model, label, event) {
        $scope.loadFirma(item.id);
    }
    $scope.saveChanges = function () {
        if($scope.editMode) {
            var push_object = Object.assign({}, $scope.firma);
            push_object.grad_fk = $scope.firma.grad_fk.id;
            push_object.slika_zaglavlje = '-';
            if ($scope.logoFile) {
                push_object.logo = $scope.logoFile;
                Upload.upload({
                    url: '/api/firma/' + push_object.id + '/',
                    data: {
                        id_broj: push_object.id_broj,
                        naziv: push_object.naziv,
                        pdv_broj: push_object.pdv_broj,
                        adresa: push_object.adresa,
                        logo: $scope.logoFile
                    },
                    method: 'PUT'
                }).then(function (response) {
                    // @TODO ovdje treba prikazati poruku o uspjesnom update
                });
            }
            delete push_object.logo;
            Firma.update(push_object, function (data, respHead) {
                // @TODO ovdje treba prikazati poruku o uspjesnom update
            });
        }
        $scope.editMode = !$scope.editMode;
    };
    $scope.loadFirma = function (firmaId) {
        $scope.firma = Firma.get({id: firmaId}, function () {
            $scope.firma.grad_fk = Grad.get({id: $scope.firma.grad_fk});
            $scope.firma.logo = !$scope.firma.logo ? '/media/logo.png' : $scope.firma.logo;
            Grad.get({}, function (data) {
                $scope.gradovi = data.results;
            });
        });
    }


    $scope.claimFirma = function () {
        $scope.firma.admin_fk = $scope.korisnik.id;
        var push_object = Object.assign({}, $scope.firma);
        push_object.grad_fk = $scope.firma.grad_fk.id;
        delete push_object.logo;
        Firma.update(push_object, function (data, respHead) {
            // @TODO ovdje treba prikazati poruku o uspjesnom update
        });
    }
    $scope.selectLogo = function (file, errFiles) {
        $scope.logoFile = file;
    }
    $scope.loadFirma($routeParams['firmaId']);
})
app.run(function($rootScope, $http, $location) {
    $rootScope.go = function (path) {
        $location.path(path);
    };
    $rootScope.parseUrl = function (url) {
        $scope.parser = document.createElement('a');
        $scope.parser.href = url;
        return $scope.parser;
    }
    $rootScope.location = $location;
    $rootScope.isLoggedIn = function (callback=null, data=null) {
        return $http.get('/korisnik/')
            .then(function(response) {
                $rootScope.korisnik = response.data.korisnik;
                if (callback) {
                    data ? callback(data) : callback();
                };
        });
    };
    $rootScope.dispatcher = [];
    $rootScope.loop = function () {
        for (var i = 0; i < $rootScope.dispatcher.length; i++) {
            $rootScope.dispatcher[i]();
        };
        $rootScope.dispatcher = [];
    }
    $rootScope.$on('$routeChangeStart', function(event, next, current) {
        $rootScope.isLoggedIn().then(function () {
            if ($rootScope.korisnik && ($location.path() == '/korisnik/novi' || $location.path() == '/login')) {
                $location.path('/');
            }
        });
    });
    $rootScope.isLoggedIn();
});
app.controller('ProfilCtrl', function ($scope, $routeParams, Osoba, User, Upload) {
    $scope.loadOsoba = function (osobaId) {
        osobaId = !osobaId ? $scope.korisnik.id : osobaId;
        $scope.user = {}
        user = User.get({id: osobaId}, function () {
            $scope.user = user ? user : $scope.user;
            osoba = Osoba.get({id: $scope.user.id}, function () {
                $scope.osoba = osoba ? osoba : $scope.osoba;
                $scope.osoba.slika = !$scope.osoba.slika ? '/media/profile.png' : $scope.osoba.slika;
            });
        });
    };
    $scope.saveKontakt = function () {
        $scope.noviKontaktEdit = !$scope.noviKontaktEdit;
    }
    $scope.saveChanges = function () {
        if($scope.editMode) {
            var push_object = Object.assign({}, $scope.osoba);
            delete push_object.slika;
            Osoba.update(push_object, function (data, respHead) {
               if ($scope.slikaFile) {
                    push_object.slika = $scope.slikaFile;
                    Upload.upload({
                        url: '/api/osoba/' + push_object.id + '/',
                        data: {
                            ime: push_object.ime,
                            prezime: push_object.prezime,
                            slika: $scope.slikaFile,
                            user_fk: push_object.user_fk
                        },
                        method: 'PUT'
                    }).then(function (response) {
                        // @TODO ovdje treba prikazati poruku o uspjesnom update
                    });
                }
            });
        }
        $scope.editMode = !$scope.editMode;
    };
    $scope.selectSlika = function (file, errFiles) {
        $scope.slikaFile = file;
    }
    $scope.loadOsoba($routeParams['osobaId']);
});
app.controller('LoginCtrl', function($scope, $http, $cookies) {
    $scope.submit = function() {
        $scope.formData.csrfmiddlewaretoken = $cookies.get('csrftoken');
        if ($scope.formData) {
            $http({
                method: 'POST',
                url: '/korisnici/login/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                transformRequest: function(obj) {
                    var str = [];
                    for (var p in obj) {
                        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                    }
                    return str.join("&");
                },
                data: $scope.formData
            }).success(function(response) {
                $scope.isLoggedIn().then(function () {
                    $scope.go('/');
                });
            }).error(function() {
                console.error('An error occured during submission');
            });
        }
        return false;
    };
});
app.controller('LogoutCtrl', function($scope, $http) {
    $scope.logout = function () {
        $http({
            method: 'GET',
            url: '/korisnici/logout/'
        }).then(function successCallback(response) {
            $scope.go('/korisnici/login')
        }, function errorCallback(response) {
            console.error('An error occured during get');
        });
    };
});
app.controller('RegisterCtrl', function($scope, $http, $window, $cookies, djangoForm) {
    $scope.submit = function() {
        $scope.registration_data.csrfmiddlewaretoken = $cookies.get('csrftoken');
        $scope.registration_data.captcha_0 = $('#id_captcha_0').val();
        $scope.registration_data.captcha_1 = $('#id_captcha_1').val();
        console.log($scope.registration_data);
        if ($scope.registration_data) {
            $http({
                method: 'POST',
                url: '/korisnici/novi/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                transformRequest: function(obj) {
                    var str = [];
                    for(var p in obj)
                        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                    return str.join("&");
                },
                data: $scope.registration_data
            }).success(function(response) {
                if (!djangoForm.setErrors($scope.registration_form, response.errors)) {
                    // var bodyHtml = /<body.*?>([\s\S]*)<\/body>/.exec(response)[1];
                    // $('body').html(bodyHtml);
                    $scope.go('/');
                }
            }).error(function() {
                console.error('An error occured during submission');
            });
        }
        return false;
    };
});
app.controller('Ctrl', function ($scope, $translate) {
    $scope.changeLanguage = function (key) {
        $translate.use(key);
    };
});
