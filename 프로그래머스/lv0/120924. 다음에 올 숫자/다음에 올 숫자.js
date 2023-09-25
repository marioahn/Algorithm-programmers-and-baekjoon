function solution(common) {
    // 등차인 경우
    if (common[2]-common[1] === common[1]-common[0]) {
        return common.at(-1)+(common[1]-common[0])
    }
    // 등비인 경우
    else {
        return common.at(-1)*(common[1]/common[0])
    }
}