# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_list = list(map(int, input().split()))

unique_rooms = set(room_list)
captain_room = (sum(unique_rooms) * k - sum(room_list)) // (k - 1)
print(captain_room)