-- vim:set foldmethod=marker:
-- require "lfs"
-- cwd = lfs.currentdir()
-- -- aaa = lfs.dir(".\\pad_searcher.moon")
-- -- chg_cwd = aaa.."\\?.lua;"..package.path
-- print cwd
-- print chg_cwd

module "pad_searcher", package.seeall
require "pad_node"

node_a = pad_node.Node 1, "aaaa"

print unpack node_a.route
