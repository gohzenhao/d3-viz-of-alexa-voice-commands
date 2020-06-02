// ****** configuration of aws services
var amazonRegion = "ap-southeast-2";
var identityPoolId = "ap-southeast-2:9516c8d5-767d-47f8-8196-2320fe7170c0";

AWS.config.update({
	region: amazonRegion,
	credentials: new AWS.CognitoIdentityCredentials({
		IdentityPoolId: identityPoolId
	})
});

AWS.config.credentials.get(function(err) {
	if (err) alert(err);
	console.log(AWS.config.credentials);
});

// ****** dynamoDb access

var docClient = new AWS.DynamoDB.DocumentClient({apiVersion: '2012-08-10'});

// call this function whenever you want to retrieve data from the db
// it gives you the complete contents of the database
function queryData() {
    var promise1 = new Promise( (resolve, reject) => {

        var params = {
            TableName : "chatdiarytest-DynamoDBTable-1PC4FXBN51C26",
        };

        docClient.scan(params, function(err, data) {
            if (err) {
                reject("FAILED!");
            } else {
                console.log(data);
                resolve(data);
            }
        });
});
}