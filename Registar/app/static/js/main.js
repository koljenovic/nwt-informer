var app = angular.module('kontakt', ['ngRoute', 'ngResource', 'djng.forms', 'pascalprecht.translate', 'ui.bootstrap', 'ngCookies', 'ngAnimate']);
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
app.controller('PageCtrl', function ($scope, $http, $location, Firma, Grad) {
    $scope.search = function (searchString) {
        return $http.get('/search/', { params: { 'text__startswith': searchString }})
            .then(function(response) {
                return response.data.results.slice(0, 5);
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
            Firma.update(push_object, function (data, respHead) {
                // @TODO ovdje treba prikazati poruku o uspjesnom update
            });
        }
        $scope.editMode = !$scope.editMode;
    };
    $scope.loadFirma = function (firmaId) {
        $scope.firma = Firma.get({id: firmaId}, function () {
            $scope.firma.grad_fk = Grad.get({id: $scope.firma.grad_fk});
            $scope.firma.logo = !$scope.firma.logo ? 'logo.png' : $scope.firma.logo;
            Grad.get({}, function (data) {
                $scope.gradovi = data.results;
            });
        });
    }
    $scope.loadFirma(3);
})
app.run(function($rootScope, $http, $location) {
    $rootScope.go = function (path) {
        $location.path(path);
    };
    $rootScope.isLoggedIn = function () {
        return $http.get('/korisnik/')
            .then(function(response) {
                $rootScope.korisnik = response.data.korisnik;
        });
    };
    $rootScope.$on('$routeChangeStart', function(event, next, current) {
        $rootScope.isLoggedIn().then(function () {
            if ($rootScope.korisnik && ($location.path() == '/korisnik/novi' || $location.path() == '/login')) {
                $location.path('/');
            }
        });
    });
});
app.controller('ProfilCtrl', function ($scope, $routeParams, Osoba, User) {
    $scope.loadOsoba = function (osobaId) {
        osobaId = !osobaId ? $scope.korisnik.id : osobaId;
        $scope.user = {}
        $scope.osoba = {'id': osobaId, 'ime': 'ime', 'prezime': 'prezime', 'slika': 'profile.png', 'mock': true};
        osoba = Osoba.get({id: osobaId}, function () {
            $scope.osoba = osoba ? osoba : $scope.osoba;
            $scope.osoba.slika = !$scope.osoba.slika ? 'profile.png' : $scope.osoba.slika;
        });
        user = User.get({id: osobaId}, function () {
            $scope.user = user ? user : $scope.user;
        });
    };
    $scope.saveKontakt = function () {
        $scope.noviKontaktEdit = !$scope.noviKontaktEdit;
    }
    $scope.saveChanges = function () {
        if($scope.editMode) {
            var push_object = Object.assign({}, $scope.osoba);
            if ($scope.osoba.mock) {
                Osoba.save(push_object, function (data, respHead) {
                    // @TODO ovdje treba prikazati poruku o uspjesnom update
                });
            } else {
                Osoba.update(push_object, function (data, respHead) {
                    // @TODO ovdje treba prikazati poruku o uspjesnom update
                });
            }
        }
        $scope.editMode = !$scope.editMode;
    };
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
                    for(var p in
obj)
                        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                    return str.join("&");
                },
                data: $scope.formData
            }).success(function(response) {
        $scope.isLoggedIn().then ( function() {
                $scope.go('/');
            }
        )
                // var bodyHtml = /<body.*?>([\s\S]*)<\/body>/.exec(response)[1];
                // $('body').html(bodyHtml);
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
