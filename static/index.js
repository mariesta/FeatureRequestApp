var FeatureviewModel = {
    name : ko.observable(""),
    description : ko.observable(""),
    clientValues : [
    	{name: "Client A", id: 1},
    	{name: "Client B", id: 2},
    	{name: "Client C", id: 3}
    ],
    selectedClient : ko.observable(1),
    priority : ko.observable(1),
    target : ko.observable(null),
    areaValues : [
    	{name: "Policies", id: "policy"},
    	{name: "Billings", id: "billing"},
    	{name: "Claims", id: "claim"},
    	{name: "Reports", id: "report"}
    ],
    selectedArea : ko.observable('policy'),
    doSomething : function(formElement) {
    	// If the form data is valid, post the serialized form data to the web API.
        $(formElement).validate();
        if ($(formElement).valid()) {
            $.ajax({
	            url: '/createFeature',
	            data: $(formElement).serialize(),
	            type: 'POST',
	            success: function(response) {
	                console.log(response);
	            },
	            error: function(error) {
	                console.log(error);
	            }
	        });
        }
    }
};
ko.applyBindings(FeatureviewModel);