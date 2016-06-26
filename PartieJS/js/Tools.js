/**
  * Fonction d'orientation de message entrant
  */
var rxTools = {
//Orientation du message reçu
	rxRouting : function (scope,rootScope,data){
        var mType = data.messageType;
        
        switch(mType) {
            case "treeForShow":
//                alert(data.message);
            	manageRxTree.getTree(scope,data);
                break;
            
            default:
                alert("Type de message inconnue!");
            	console.info("ORNI: ",data);
        }
    }
        
};
var manageRxTree = {
		getTree: function (scope,jsonData){
			scope.majCatego(jsonData.treeBookMark);
		}//,
}

