#25/03/2020
k = int(input())

roomList = list(map(int,input().split()))
print(f"roomList: {roomList}")
roomSet = set(roomList)
print(f"roomSet :{roomSet}")

sumRoomList = sum(roomList)
print(f"sumRoomList :{sumRoomList}")
sumRoomSet = sum(roomSet)
print(f"sumRoomSet :{sumRoomSet}")
temp = sumRoomSet*k - sumRoomList
print(f"temp :{temp}")
ans = temp/(k-1)
print(int(ans))