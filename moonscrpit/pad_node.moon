-- vim:set foldmethod=marker:

module "pad_node", package.seeall
export Node

class Node
	new: (start, @board) =>-- {{{
		@score = 0
		@combo = 0
		@route = {}
		table.insert(@route, start)-- }}}
	show_route: =>
		print unpack @route
	set_route: (route_lst) =>-- {{{
		@route = {}
		for r = 1, #route_lst
			table.insert(@route, r)-- }}}
    -- }}}

-- node_a = Node 1, "aaaaaa"

-- print unpack node_a.route
-- node_a\show_route!
--
-- route_lst = {1, 2, 3, 4, 5}
--
-- node_a\set_route route_lst
-- print unpack node_a.route

