import NavbarController from './navbar.controller';

class NavbarDirective {
    constructor () {
        'ngInject';

        return  {
            'restrict': 'E',
            'templateUrl': 'app/components/navbar/navbar.html',
            'controller': NavbarController,
            'controllerAs': 'vm',
            'bindToController': true
        };
    }
}


export default NavbarDirective;
