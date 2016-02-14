local f = io.open("get_cwd.py", "w")
f:write("import os; print os.path.dirname(__file__)")
f:close()

-- local handle = io.popen("python get_cwd.py")
-- local result = handle:read("*")
-- handle:close()
--
-- print(result)
