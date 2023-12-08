
rm -f /opt/ready.flag

echo -e ""
echo -e "\033[97m----------------------------------------\033[00m"
echo -e "\033[94m[+] Configure mongo cluster\033[00m"
echo -e "$\033[97m----------------------------------------\033[00m"
echo -e "\033[92m[*] Step 1 from 7\033[00m"
echo "rs.initiate({_id: \"mongors1conf\", configsvr: true, members: [{_id: 0, host: \"mongocfg1\"}, {_id: 1, host: \"mongocfg2\"}, {_id: 2, host: \"mongocfg3\"}]})" | mongosh "mongodb://mongocfg1:27017"
echo -e "\033[92m[*] Step 2 from 7\033[00m"
echo "rs.initiate({_id: \"mongors1\", members: [{_id: 0, host: \"mongors1n1\"}, {_id: 1, host: \"mongors1n2\"}, {_id: 2, host: \"mongors1n3\"}]})" | mongosh "mongodb://mongors1n1:27017"
sleep 10
echo -e "\033[92m[*] Step 3 from 7\033[00m"
echo "sh.addShard(\"mongors1/mongors1n1\")" | mongosh "mongodb://mongos1:27017"
echo -e "\033[92m[*] Step 4 from 7\033[00m"
echo "rs.initiate({_id: \"mongors2\", members: [{_id: 0, host: \"mongors2n1\"}, {_id: 1, host: \"mongors2n2\"}, {_id: 2, host: \"mongors2n3\"}]})" | mongosh "mongodb://mongors2n1:27017"
sleep 10
echo -e "\033[92m[*] Step 5 from 7\033[00m"
echo "sh.addShard(\"mongors2/mongors2n1\")" | mongosh "mongodb://mongos1:27017"

echo -e ""
echo -e "\033[97m----------------------------------------\033[00m"
echo -e "\033[94m[+] Create database\033[00m"
echo -e "$\033[97m----------------------------------------\033[00m"
echo -e "\033[92m[*] Step 6 from 7\033[00m"
echo "use recommender" | mongosh "mongodb://mongors1n1:27017"
echo -e "\033[92m[*] Step 7 from 7\033[00m"
echo "sh.enableSharding(\"recommender\")" | mongosh "mongodb://mongos1:27017"
echo -e "\033[92m[*] Set ready.flag\033[00m"
echo "MONGO CLUSTER IS READY" > /opt/ready.flag
echo -e "\033[92m[*] Wait healthcheck\033[00m"
sleep 30
echo -e "\033[92m[*] The END\033[00m"