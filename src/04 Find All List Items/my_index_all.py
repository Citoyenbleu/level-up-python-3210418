def index_all(search_list, pattern):
  index_list = []

  for index, value in enumerate(search_list):
    if value == pattern:
      index_list.append([index])
    elif isinstance(search_list[index], list):
      for sub_index in index_all(search_list[index], pattern):
        index_list.append([index] + sub_index)

  return index_list

# l = [[0, 1, 2], 2, [4,5], [1,2,3,4]]
# l = [0,1,2,3,2]
l = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

n = 2
print(index_all(l, n))
print(index_all(l, [1,2,3]))