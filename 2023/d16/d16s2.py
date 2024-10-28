
class direction:
    right = 0
    left = 1
    up = 2
    down = 3

class directionalVisit():
    right = False
    left = False
    up = False
    down = False

# each beam is defined by its location and its direction [i,j, direction]
class Beam:
    def __init__(self, _i: int, _j: int, _d: int):
        self.i = _i
        self.j = _j
        self.d = _d

    i: int
    j: int
    d: int


class Solution:

    def __init__(self, gridlines, i: int, j: int, d: int):
        
        self.grid = gridlines
        self.m = len(self.grid)
        self.n = len(self.grid[0])
        # be sure to add check for initial direction here
        self.beams = [Beam(i,j, d)]
        self.visited = [[directionalVisit() for j in range(self.n)] for i in range(self.m)]
        match d:
            case direction.right:
                self.visited[i][j].right = True
            case direction.left:
                self.visited[i][j].left = True
            case direction.up:
                self.visited[i][j].up = True
            case direction.down:
                self.visited[i][j].down = True
        self.updateDirection(self.beams[0])

    def propogate(self, beam: Beam):
        match beam.d:
            case direction.right:
                beam.j += 1
            case direction.left:
                beam.j -= 1
            case direction.up:
                beam.i -= 1
            case direction.down:
                beam.i += 1

    def terminate(self, beam: Beam) -> bool:
        match beam.d:
            case direction.right:
                return True if beam.j >= self.n-1 else False
            case direction.left:
                return True if beam.j <= 0 else False
            case direction.up:
                return True if beam.i <= 0 else False
            case direction.down:
                return True if beam.i >= self.m-1 else False

    def isBeamReduntant(self, beam: Beam) -> bool:
        return (beam.d == direction.right and self.visited[beam.i][beam.j].right) \
                or (beam.d == direction.left and self.visited[beam.i][beam.j].left) \
                or (beam.d == direction.up and self.visited[beam.i][beam.j].up) \
                or (beam.d == direction.down and self.visited[beam.i][beam.j].down)

    def updateVisited(self, beam: Beam):
        match beam.d:
            case direction.right:
                self.visited[beam.i][beam.j].right = True
            case direction.left:
                self.visited[beam.i][beam.j].left = True
            case direction.up:
                self.visited[beam.i][beam.j].up = True
            case direction.down:
                self.visited[beam.i][beam.j].down = True

    def updateDirection(self, beam: Beam):
        tile = self.grid[beam.i][beam.j]
        match tile:
            case '/':
                match beam.d:
                    case direction.right:
                        beam.d = direction.up
                    case direction.left:
                        beam.d = direction.down
                    case direction.up:
                        beam.d = direction.right
                    case direction.down:
                        beam.d = direction.left
            case '\\':
                match beam.d:
                    case direction.right:
                        beam.d = direction.down
                    case direction.left:
                        beam.d = direction.up
                    case direction.up:
                        beam.d = direction.left
                    case direction.down:
                        beam.d = direction.right
            case '|':
                match beam.d:
                    case direction.right | direction.left:
                        beam.d = direction.up
                        self.beams.append(Beam(beam.i, beam.j, direction.down))

            case '-':
                match beam.d:
                    case direction.up | direction.down:
                        beam.d = direction.right
                        self.beams.append(Beam(beam.i, beam.j, direction.left))

    def propogateBeam(self):
        beam = self.beams[0]
        # make sure next tile exists and is not redundant
        if self.terminate(beam):
            self.beams.pop(0)
        else:
            # move into next tile
            self.propogate(beam)
            if self.isBeamReduntant(beam):
                self.beams.pop(0)
            else:
                # update visited
                self.updateVisited(beam)
                # update direction
                self.updateDirection(beam)

    def printEnergizedTiles(self):
        for row in self.visited:
            for tile in row:
                if tile.right or tile.left or tile.up or tile.down:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')

    def energizedTiles(self) -> int:
        count = 0
        for row in self.visited:
            for tile in row:
                if tile.right or tile.left or tile.up or tile.down:
                    count += 1
        return count

    
    m: int # len(grid)
    n: int # len(grid[0])
    grid: list
    visited: list[list[directionalVisit]]
    beams: list[Beam]


input_file = "input.txt"

with open(input_file, "r") as data:
    gridlines = data.readlines()
gridlines = [line.strip('\n') for line in gridlines]

maxEnergy = 0
for i in range(len(gridlines)):
    solution = Solution(gridlines, i, 0, direction.right)
    while solution.beams:
        solution.propogateBeam()
    if maxEnergy < solution.energizedTiles():
        maxEnergy = solution.energizedTiles()

for i in range(len(gridlines)):
    solution = Solution(gridlines, i, len(gridlines[0])-1, direction.left)
    while solution.beams:
        solution.propogateBeam()
    if maxEnergy < solution.energizedTiles():
        maxEnergy = solution.energizedTiles()

for j in range(len(gridlines[0])):
    solution = Solution(gridlines, len(gridlines)-1, j, direction.up)
    while solution.beams:
        solution.propogateBeam()
    if maxEnergy < solution.energizedTiles():
        maxEnergy = solution.energizedTiles()

for j in range(len(gridlines[0])):
    solution = Solution(gridlines, 0, j, direction.down)
    while solution.beams:
        solution.propogateBeam()
    if maxEnergy < solution.energizedTiles():
        maxEnergy = solution.energizedTiles()

print("How many tiles end up being energized?", maxEnergy)