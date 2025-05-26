# Define variables for database connection and file path
$server = "$env:SERVER"
$database = "$env:DATABASE"
$user = "$env:USER"
$password = "$env:PASS"
$table = "[staging].[stations]"
$data = "$env:DATA"
$file = "-10_-10_-20_00"

# Execute the bcp command to load data
bcp ${table} in ${data}\${file}_pre.csv -d ${database} -S "${server}" -e ${data}\${file}_pre.err -G -U "${user}" -P ${password} -f ${data}\stations.fmt -F 2