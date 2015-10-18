/* global _:false, moment:false */
import config from './index.config';
import routerConfig from './index.route';
import runBlock from './index.run';

/* Controllers */
import MainController from './main/main.controller';

/* Directives */
import NavbarDirective from '../app/components/navbar/navbar.directive';


const modules = [
    'ngAnimate',
    'ngCookies',
    'ngTouch',
    'ngSanitize',

    'restangular',
    'ngRoute',
    'ngMaterial'
];

angular.module('monarch', modules)
    .constant('_', _)
    .constant('moment', moment)

    .config(config)
    .config(routerConfig)
    .run(runBlock)

    /* Services */

    /* Controllers */
    .controller('MainController', MainController)

    /* Directives */
    .directive('moNavbar', () => new NavbarDirective());
