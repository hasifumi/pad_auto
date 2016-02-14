-- function exce_command(command)
function exce_command()
 	local command = 'python .\\get_cwd.py'
	local handle = io.popen(command, "r")
	local content = handle:read("*a")
	print(content)
	handle:close()
	return content
end

print(exce_command())

-- function exec_get_cwd_py()
-- 	local command = "python ./get_cwd.py"
-- 	local command_result = exce_command(command)
-- 	print(command_result)
-- end
