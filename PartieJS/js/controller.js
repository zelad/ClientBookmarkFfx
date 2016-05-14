
/**
 * mon test avec ces problèmes de "cross origine"
 */
var app = angular.module('uneApp', []);

app.controller("uneFonctionCtrl", function ($scope, $rootScope,$http, WebSocketService) {

	
/**
 * Partie Template
 */	
//Mise en place du Socket
	$rootScope.ws = new SocketManager.SocketManager($scope,$rootScope);
	
//	$scope.fireWStest = function(){
////		$rootScope.ws.send("test");
//		WebSocketService.sendObject("recAttack","toto");
//	};

});


var SocketManager = {
	ws:{},
	
	SocketManager: function (scope,rootScope){
        this.ws = new WebSocket("ws://localhost:9999/");
//        this.ws = new WebSocket("ws://localhost:80/");
        
        this.ws.onopen = function(){
        	console.log("Socket has been opened!");
        };
        
    	this.ws.onmessage = function(message) {
console.log(message);
//    	    var messageObj = JSON.parse(message.data);
    	    
//  console.log("Received data from websocket: ", messageObj);
//    	    rxTools.rxRouting(scope,rootScope,messageObj);
    	};
        
        return this.ws;
    }
	
};
