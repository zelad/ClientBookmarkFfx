/**
 * Test d'enregistrement de fichier
 */

var app = angular.module('uneApp', ['angularBootstrapNavTree']);

app.controller("uneFonctionCtrl", function ($scope, $rootScope,$timeout, WebSocketService) {
	
	$rootScope.ws = new SocketManager.SocketManager($scope,$rootScope);

	txLogin = function() {
		WebSocketService.sendObject("login",null);
	}
	
$scope.data = [];

/**
 * Apparition d'éléments suite à une "event"
 */
//MAJ des listes de catégorie
	$scope.majCatego = function (list) {
		$timeout(function () {
			$scope.data = list;
		}, 100);
	}
	
});

var SocketManager = {
		ws:{},
		
		SocketManager: function (scope,rootScope){
	        this.ws = new WebSocket("ws://localhost:9999/");
	        
	        this.ws.onopen = function(){
	        	console.log("Socket has been opened!");
	        	txLogin();
	        };
	        
	    	this.ws.onmessage = function(message) {
	//console.log(message);
	    	    var messageObj = JSON.parse(message.data);
	    	    
	  console.log("Received data from websocket: ", messageObj);
	    	    rxTools.rxRouting(scope,rootScope,messageObj);
	    	};
	        
	        return this.ws;
	    }
		
};

