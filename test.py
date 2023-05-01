import json;
import requests;

#file = open(r"C:\Users\rohimatw\Downloads\New JESI Task\New JESI Task\CellularCustomers_Details_20210921Z234510Z.json")

#test = "[{\"Start Date\":\"account1886841\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"Monthly_Price_Zero_sub9023791\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c4\",\"Plan\":\"150GB\",\"Usage\":\"113.2GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account7056991\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"Monthly_Price_Zero_sub6629561\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c5\",\"Plan\":\"230GB\",\"Usage\":\"215.1GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account4902531\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub4028991\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c6\",\"Plan\":\"100GB+20GB\",\"Usage\":\"144GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account7922961\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub1061731\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c7\",\"Plan\":\"30GB\",\"Usage\":\"8GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account1094411\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub8963911\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c8\",\"Plan\":\"60GB\",\"Usage\":\"66.3GB\",\"Supervisioning Status\":\"Cancelled\"},{\"Start Date\":\"account2898901\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub5203411\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c9\",\"Plan\":\"30GB+20GB\",\"Usage\":\"46.7GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account7892781\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub177001\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c10\",\"Plan\":\"180GB+20GB\",\"Usage\":\"177GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account3356281\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub6067511\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c11\",\"Plan\":\"100GB+100GB\",\"Usage\":\"163.8GB\",\"Supervisioning Status\":\"Active\"},{\"Start Date\":\"account4829581\",\"End Date\":\"2020-06-19T15:31:47Z\",\"Subscription ID\":\"inactive_200_sub3195731\",\"Partner Subscription ID\":\"a829b-8de923-c3748-def92a-3c12\",\"Plan\":\"35GB\",\"Usage\":\"33.5GB\",\"Supervisioning Status\":\"Cancelled\"}]";

#json_data = json.load(file)

#js_data = json.loads(test)


testStr = '''[{
	"Start Date": "account1886841",
	"End Date": "2020-06-19T15:31:47Z",
	"Subscription ID": "Monthly_Price_Zero_sub9023791",
	"Partner Subscription ID": "a829b-8de923-c3748-def92a-3c4",
	"Plan": "150GB",
	"Usage": "113.2GB",
	"Supervisioning Status": "Active"
}]'''

js_data = json.loads(testStr)


# Add keys to extract from JSON Object in order to create request string
requestKeys = ['Start Date', 'Subscription ID', 'End Date'] 
 
for request in js_data:
    eachRequest = dict(request)
    #print(eachRequest)
    updatedRequest = {x:eachRequest[x] for x in requestKeys}
    reqStr =  f'[' + str(updatedRequest) + ']'
    str = json.dumps(reqStr)
    print(str)
    


    




 
