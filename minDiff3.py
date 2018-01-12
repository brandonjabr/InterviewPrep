def minDiff3(A, B, C):
    i, j, k = 0, 0, 0
    ans = max(A[i],B[j],C[k]) - min(A[i],B[j],C[k])
    while i < len(A) and j < len(B) and k < len(C):
        minVal = min(A[i],B[j],C[k])
        maxVal = max(A[i],B[j],C[k])
        if maxVal - minVal < ans:
            ans = maxVal - minVal
        if ans == 0:
            break
        if A[i] == minVal:
            i += 1
        elif B[j] == minVal:
            j += 1
        else:
            k += 1
    return ans

A = [ -18, 0, 38, 42, 91, 94, 129, 152, 169, 204, 204, 225, 253, 298, 309, 343, 344, 370, 400, 409, 424, 459, 480, 485, 513, 518, 531, 534, 542, 553, 564, 573, 594, 639, 663, 679, 712, 731, 743, 778, 815, 841, 868, 911, 950, 972, 987, 1000, 1029, 1033, 1047, 1096, 1124, 1168, 1171, 1178, 1196, 1217, 1256, 1263, 1291, 1304, 1314 ]
B = [ 36, 38, 38, 74, 84, 105, 121, 156, 170, 179, 191, 227, 249, 296, 315, 356, 366, 374, 415, 443, 451, 459, 472, 498, 505, 509, 558, 600, 619, 661, 684, 715, 754, 782, 796, 805, 815, 853, 868, 871, 891, 925, 929, 967, 999, 1006, 1006, 1048, 1059, 1092, 1132, 1175, 1221, 1252, 1290, 1331, 1361, 1406, 1444, 1462, 1487, 1526, 1572, 1586, 1629, 1647, 1690, 1692, 1704, 1734, 1757, 1773, 1810, 1823, 1846, 1860 ]
C = [ 0, 27, 57, 94, 102, 116, 140, 166, 207, 233, 239, 268, 296, 332, 343, 382, 383, 398, 411, 435, 444, 472, 486, 523, 531, 574, 597, 600, 607, 641, 651, 677, 692, 725, 728, 734, 736, 767, 793, 797, 832, 874, 904, 933, 938, 947, 961, 988, 1035, 1047 ]
print minDiff3(A,B,C)