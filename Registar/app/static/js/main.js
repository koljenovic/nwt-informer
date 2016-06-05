var app = angular.module('kontakt', ['ngRoute', 'ngResource', 'djng.forms', 'pascalprecht.translate', 'ui.bootstrap', 'ngCookies', 'ngAnimate', 'ngFileUpload']);
app.config(function ($interpolateProvider, $translateProvider, $resourceProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{-');
    $interpolateProvider.endSymbol('-}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $translateProvider.translations('en', {
        team: 'Team',
        contacts: 'Contacts',
        logout: 'Logout',
        edit_profile: 'Edit profile',
        save_changes: 'Save changes',
        claim_profile: 'Claim profile',
        register: 'Register',
        directory_add: 'Favorite',
        login: 'Log in',
        kontakt_podaci: 'Contact data',
        legalese: 'Legal disclaimer',
        search_text: 'Find public data about a company or person:',
        home: 'Home',
        about: 'About',
        contact: 'Contact',
    });
    $translateProvider.translations('bs', {
        team: 'Tim',
        contacts: 'Kontakti',
        logout: 'Odjavi se',
        edit_profile: 'Uredi profil',
        save_changes: 'Spremi izmjene',
        claim_profile: 'Preuzmi profil',
        register: 'Registruj se',
        directory_add: 'Dodaj u imenik',
        login: 'Prijavi se',
        kontakt_podaci: 'Kontakt podaci',
        legalese: 'Pravno ograđivanje',
        search_text: 'Pronađi javne podatke o pravnom ili fizičkom licu:',
        home: 'Početna',
        about: 'O aplikaciji',
        contact: 'Kontakt',
    });
    $translateProvider.preferredLanguage('bs');
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
app.controller('PageCtrl', function ($scope, $http, $routeParams, $location, $translate, Upload, Firma, Grad, Osoba, User) {
    $scope.changeLanguage = function (key) {
        $translate.use(key);
    };

/* 
	****** DODAVANJE OSOBA U TIM - POČETAK ****** 
*/     
    $scope.isCollapsed = true;
    $scope.success = "";
    $scope.idFirma = $routeParams['firmaId'];
    $scope.timData = {};

	// dobavljanje broja uloga u tabeli app_uloga
    $.ajax({
        url: '/api/uloga/',
        method: 'GET'
    }).then(function(data) {
        $scope.tmp = data.results;
        $scope.$apply(function() {
            $scope.tmp.push(data.results);
            $scope.brUloga = $scope.tmp.length - 1;
        });
    });
    
	  
  	$scope.joinTeam = function () {
  		$http({method: 'POST', url: '/currentuser/'}).
		success(function(data){
			$scope.idUser = data.user;
			$scope.ulogaId = $scope.brUloga + 1;
			
			var foo = {id : $scope.ulogaId,
                       naziv_uloge : $scope.timData.uloga,
                       firma_fk : $scope.idFirma,
                       user_fk : $scope.idUser  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);
			
			$http({
            method  : 'POST',
            url     : '/api/uloga/',
            data    : $.param(jsonObject),  
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
            })
            .success(function(data) {
                $scope.success = "Uspješno ste dodani u tim!";
                $scope.izlistajClanoveTima();
            }).error(function(data) {
            	alert(jsonString);
            	$scope.failed = "Greška!";
            });
			
		})
		.error (function(data){
			alert(data);
		});
		
		
  	};
    
/* 
	****** DODAVANJE OSOBA U TIM - KRAJ ****** 
*/



/* 
	****** IZLISTAVANJE KONTAKATA FIRME NA STRANICI FIRME - POČETAK ****** 
*/
	$scope.izlistajKontakte = function() {
		$.ajax({
		    url: '/api/kontakt/',
		    method: 'GET'
		}).then(function(data) {
		    $scope.temp = data.results;
		    $scope.$apply(function() {
		        $scope.temp.push(data.results);
		        $scope.quantity = $scope.temp.length - 1;

		        $scope.kontakti = [];
		        $scope.kategorije = [];
		        for (var i=0; i<$scope.quantity; i++) {
		            if ($scope.temp[i].firma_fk == $routeParams['firmaId']) {
		                $scope.kontakti.push($scope.temp[i]);
		                if($scope.kategorije.indexOf($scope.temp[i].naziv) == -1)
		                    $scope.kategorije.push($scope.temp[i].naziv);
		            }
		        }
		    });
		});
    };
    
    $scope.izlistajKontakte();
/* 
	****** IZLISTAVANJE KONTAKATA FIRME NA STRANICI FIRME - KRAJ ****** 
*/
    


/* 
	****** IZLISTAVANJE OSOBA U TIMU NA STRANICI FIRME - POČETAK ****** 
*/  
	$scope.izlistajClanoveTima = function() { 
		$.ajax({
		    url: '/api/uloga/',
		    method: 'GET'
		}).then(function(data) {
		    $scope.dummy = data.results;
		    $scope.$apply(function() {
		        $scope.dummy.push(data.results);
		        $scope.brUloga = $scope.dummy.length - 1;

		        $scope.nazivuloge = [];
		        $scope.userid = [];
		        for (var i=0; i<$scope.brUloga; i++) {
		            if ($scope.dummy[i].firma_fk == $routeParams['firmaId']) {
		                $scope.nazivuloge.push($scope.dummy[i].naziv_uloge);
		                $scope.userid.push($scope.dummy[i].user_fk);
		            }
		        } 


		        $.ajax({
					url: '/api/osoba/',
					method: 'GET'
				}).then(function(data) {
					$scope.dummy = data.results;
					$scope.$apply(function() {
						$scope.dummy.push(data.results);
						$scope.brOsoba = $scope.dummy.length - 1;

						$scope.osobe = [];
					 	for (var j=0; j<$scope.userid.length; j++) {
							for (var i=0; i<$scope.brOsoba; i++){
								if ($scope.dummy[i].user_fk == $scope.userid[j]) 
									$scope.osobe.push($scope.dummy[i]);
							}
						}  

						$.ajax({
							url: '/api/tim/',
							method: 'GET'
						}).then(function(data) {
							$scope.dummy = data.results;
							$scope.$apply(function() {
								$scope.dummy.push(data.results);
								$scope.brKontakta = $scope.dummy.length - 1;
							
								$scope.osobaKontakti = [];
							
							 	for (var i=0; i<$scope.osobe.length; i++) {
							 		for (var j=0; j<$scope.brKontakta; j++) {
								 		if (($scope.dummy[j].osoba_fk != null) && ($scope.dummy[j].osoba_fk == $scope.osobe[i].id)) {
								 			$scope.osobaKontakti.push($scope.dummy[j]);
										}
									}
								}

								$scope.osobeDetails = []
								for (var i=0; i<$scope.osobe.length; i++) {
									var tmp = {id : $scope.osobe[i].id,
											   ime : $scope.osobe[i].ime,
											   prezime : $scope.osobe[i].prezime,
											   uloga : $scope.nazivuloge[i]  };
									var jsonStr = JSON.stringify(tmp, null, '\t');
									var jsonObj = JSON.parse(jsonStr);
								
									$scope.osobeDetails.push(jsonObj);
								}
							
							});
						}); 
						 
					});
				});
		                    
		    });
		});
    };
    
    $scope.izlistajClanoveTima();
    
/* 
	****** IZLISTAVANJE OSOBA U TIMU NA STRANICI FIRME - KRAJ ****** 
*/  

     
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
    $scope.firmaId = $routeParams['firmaId'];
    
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
app.controller('KontaktOsobaCtrl', function ($scope, $routeParams, Osoba, User, Upload) {
    $scope.saveOsobaKontakt = function () {
        //$scope.hideKontakt = !$scope.hideKontakt;
    }
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
app.controller('KontaktCtrl', function ($scope, $http, $routeParams) {
    $scope.firmaId = $routeParams['idFirma'];
    $scope.formData = {};
    $scope.newId = $scope.quantity + 1;
    $scope.errors = false;

    $scope.processForm = function() {
        if ($scope.formData.telefon != null) {
            $scope.newId = $scope.newId + 1;
            var foo = {id : $scope.newId,
                       naziv : $scope.formData.naziv,
                       kontakt : $scope.formData.telefon,
                       vrsta_fk : 2,
                       firma_fk : $scope.firmaId  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);

            $http({
            method  : 'POST',
            url     : '/api/kontakt/',
            data    : $.param(jsonObject),  // pass in data as strings
            //data    : $scope.dataSet,
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data
            })
            .success(function(data) {


            }).error(function(data) {
                $scope.errors = true;
            });

        }

        if ($scope.formData.mobitel != null) {
            $scope.newId = $scope.newId + 1; ;
            var foo = {id : $scope.newId,
                       naziv : $scope.formData.naziv,
                       kontakt : $scope.formData.mobitel,
                       vrsta_fk : 4,
                       firma_fk : $scope.firmaId  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);
            $http({
            method  : 'POST',
            url     : '/api/kontakt/',
            data    : $.param(jsonObject),  // pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data
            })
            .success(function(data) {
                console.log(data);
            }).error(function(data) {
                $scope.errors = true;
            });
        }

        if ($scope.formData.email != null) {
            $scope.newId = $scope.newId + 1;
            var foo = {id : $scope.newId,
                       naziv : $scope.formData.naziv,
                       kontakt : $scope.formData.email,
                       vrsta_fk : 1,
                       firma_fk : $scope.firmaId  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);
            $http({
            method  : 'POST',
            url     : '/api/kontakt/',
            data    : $.param(jsonObject),  // pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data
            })
            .success(function(data) {
                console.log(data);
            }).error(function(data) {
                $scope.errors = true;
            });
        }
        if ($scope.formData.fax != null) {
            $scope.newId = $scope.newId + 1;
            var foo = {id : $scope.newId,
                       naziv : $scope.formData.naziv,
                       kontakt : $scope.formData.fax,
                       vrsta_fk : 3,
                       firma_fk : $scope.firmaId  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);
            $http({
            method  : 'POST',
            url     : '/api/kontakt/',
            data    : $.param(jsonObject),  // pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data
            })
            .success(function(data) {
                console.log(data);
            }).error(function(data) {
                $scope.errors = true;
            });
        }
        if ($scope.formData.adresa != null) {
            $scope.newId = $scope.newId + 1;
            var foo = {id : $scope.newId,
                       naziv : $scope.formData.naziv,
                       kontakt : $scope.formData.adresa,
                       vrsta_fk : 5,
                       firma_fk : $scope.firmaId  };
            var jsonString = JSON.stringify(foo, null, '\t');
            var jsonObject = JSON.parse(jsonString);
            $http({
            method  : 'POST',
            url     : '/api/kontakt/',
            data    : $.param(jsonObject),  // pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data
            })
            .success(function(data) {
                console.log(data);
            }).error(function(data) {
                $scope.errors = true;
            });
        }

        if ($scope.errors == false) {
            $scope.poruka = "Kontakt je uspješno dodan!";
            $scope.formData = {};
        }
        return false;
    };
});




