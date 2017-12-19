def delete_nth(order,max_e):
    # code here
    final = []
    for i in order:
      if final.count(i) < max_e:
        final.append(i)
    return final
