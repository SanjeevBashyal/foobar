#Level 4 Challenge 1 Escape Pods
def solution(entrances, exits, path):
    rooms=list(range(len(path)))
    exclude_rooms=set(entrances).union(set(exits))

    confirm_entries=[sum([path[j][i] for j in entrances]) for i in rooms]
    entries_intermediate_rooms=[confirm_entries[i] for i in rooms if i not in exclude_rooms]
    confirm_exits=[sum([path[i][j] for j in exits]) for i in rooms]
    exits_in_entrance=sum([confirm_exits[i] for i in rooms if i in entrances])
    exits_intermediate_rooms=[confirm_exits[i] for i in rooms if i not in exclude_rooms]

    # intermediate_rooms=rooms-entrances-exits

    reduced_path=drop(path,exclude_rooms)
    total_intermediate_rooms=len(reduced_path)

    bunnies_in_room=[0]*total_intermediate_rooms
    bunnies_exits=[0]*total_intermediate_rooms
    room_status=[0]*total_intermediate_rooms

    while 0 in room_status:
        for i in range(total_intermediate_rooms):
            bunnies=bunnies_in_room[i]
            bunnies=bunnies+entries_intermediate_rooms[i]
            if bunnies<exits_intermediate_rooms[i]:
                bunnies_exits[i]=bunnies
                room_status[i]=-1
                bunnies=0
            else:
                bunnies_exits[i]=exits_intermediate_rooms[i]
                bunnies=bunnies-bunnies_exits[i]
                transfer_bunnies,status,bunnies=bunnies_transfer_to_intermediate_rooms(room_status,reduced_path[i],bunnies)
                for j in range(len(transfer_bunnies)):
                    bunnies_in_room[j]=bunnies_in_room[j]+transfer_bunnies[j]
                room_status[i]=status
            bunnies_in_room[i]=bunnies

    return exits_in_entrance+sum(bunnies_exits)

def drop(path,exclude_rooms):
    new_path=[[path[i][j] for j in range(len(path[i])) if j not in exclude_rooms] for i in range(len(path)) if i not in exclude_rooms]
    return new_path

def bunnies_transfer_to_intermediate_rooms(room_status,path_i,bunnies_left):
    non_zero_path=[[path_i[i],i] for i in range(len(path_i)) if path_i[i]!=0]
    non_zero_path.sort()
    transfer_scheme=[0]*len(path_i)
    sufficient_flag=1
    for i in range(len(non_zero_path)):
        if bunnies_left<non_zero_path[i][0]:
            transfer_scheme[non_zero_path[i][1]]=bunnies_left
            sufficient_flag=0
            bunnies_left=0
            break
        else:
            transfer_scheme[non_zero_path[i][1]]=non_zero_path[i][0]
            bunnies_left=bunnies_left-non_zero_path[i][0]
    return transfer_scheme, sufficient_flag, bunnies_left

print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


