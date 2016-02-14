module("pad_node", package.seeall)
do
  local _class_0
  local _base_0 = {
    show_route = function(self)
      return print(unpack(self.route))
    end,
    set_route = function(self, route_lst)
      self.route = { }
      for r = 1, #route_lst do
        table.insert(self.route, r)
      end
    end
  }
  _base_0.__index = _base_0
  _class_0 = setmetatable({
    __init = function(self, start, board)
      self.board = board
      self.score = 0
      self.combo = 0
      self.route = { }
      return table.insert(self.route, start)
    end,
    __base = _base_0,
    __name = "Node"
  }, {
    __index = _base_0,
    __call = function(cls, ...)
      local _self_0 = setmetatable({}, _base_0)
      cls.__init(_self_0, ...)
      return _self_0
    end
  })
  _base_0.__class = _class_0
  Node = _class_0
  return _class_0
end
