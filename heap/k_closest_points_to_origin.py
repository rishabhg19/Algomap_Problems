class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [sqrt(pt[0]**2 + pt[1]**2) for pt in points]
        distances_mapped_to_points = defaultdict(list)
        for i in range(len(distances)):
            distances_mapped_to_points[distances[i]].append(points[i])
        print(distances_mapped_to_points)
        distances.sort()
        closest_distances = distances[:k]
        result = []
        for distance in closest_distances:
            for pt in distances_mapped_to_points[distance]:
                if k:
                    result.append(pt)
                    k -= 1
        return result