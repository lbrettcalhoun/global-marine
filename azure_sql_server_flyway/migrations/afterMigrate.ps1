# Define variables for database connection and file path
$server = "$env:SERVER.database.windows.net"
$database = "globalmarine"
$user = "$env:USER"
$password = "$env:PASS"
$table = "[staging].[stations]"
$data = "$env:DATA"

# Execute the bcp command to load data
bcp ${table} in ${data}-10_-10_-20_00.csv -d ${database} -S "${server}" -e ${$data}10_10_20_00.err -G -U "${user}" -P ${password} -f ${data}stations.fmt -F 2