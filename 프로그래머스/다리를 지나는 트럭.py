def solution(bridge_length, weight, truck_weights):
    # bridge_length 다리 길이 int
    # weight 다리가 견딜수 있는 무게 int
    # truck_weights 트럭들의 길이 list
    # bridge_length = 5
    # weight = 5
    # truck_weights = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    time = 0
    bridge = [0] * bridge_length
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append((truck_weights.pop(0)))
            else:
                bridge.append(0)
    answer = time
    return answer
