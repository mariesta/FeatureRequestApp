var featureModel = {
    name : ko.observable(""),
    description : ko.observable(""),
    clientValues : [
    	{name: "Client A", id: "A"},
    	{name: "Client B", id: "B"},
    	{name: "Client C", id: "C"}
    ],
    selectedClient : ko.observable(1),
    priority : ko.observable(1),
    target : ko.observable(moment().format("YYYY-MM-DD")),
    areaValues : [
    	{name: "Policies", id: "Policies"},
    	{name: "Billings", id: "Billings"},
    	{name: "Claims", id: "Claims"},
    	{name: "Reports", id: "Reports"}
    ],
    selectedArea : ko.observable('policy'),
    create : function(formElement) {
    	// If the form data is valid, post the serialized form data to the web API.
        $(formElement).validate();
        if ($(formElement).valid()) {
	        if (moment(this.target()) < moment()) {
	        	$('#inputTargetDate').addClass('is-invalid');
			} else {			
	            $.ajax({
		            url: '/createFeature',
		            data: $(formElement).serialize(),
		            type: 'POST',
		            success: function(response) {
		                window.location = "/";
		            },
		            error: function(error) {
		                console.log(error);
		            }
		        });
	        }
        }
    },
    deleteFeature: function(id, data, event) {
    	$.ajax({
            url: '/delete/'+ id,
            type: 'DELETE',
            success: function(response) {
                window.location = "/";
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
};
ko.applyBindings(featureModel, document.getElementById("createFeature"));