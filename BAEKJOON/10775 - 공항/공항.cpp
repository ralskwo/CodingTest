#include <iostream>
#include <vector>

using namespace std;

// Function to find the root of a gate with path compression
int find(vector<int>& parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]); // Path compression
    }
    return parent[x];
}

// Function to union two gates
void unionGates(vector<int>& parent, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    parent[rootX] = rootY; // Union by setting root of x to root of y
}

int main() {
    int G, P;
    cin >> G >> P; // Read number of gates and planes

    vector<int> parent(G + 1);
    for (int i = 1; i <= G; ++i) {
        parent[i] = i; // Initialize each gate to point to itself
    }

    int docked_planes = 0;

    for (int i = 0; i < P; ++i) {
        int gi;
        cin >> gi; // Read the preferred gate for each plane

        // Find the highest available gate for docking
        int available_gate = find(parent, gi);
        
        if (available_gate == 0) {
            break; // If no gate is available, stop processing further planes
        }

        // Dock the plane and update the availability of gates
        unionGates(parent, available_gate, available_gate - 1);
        docked_planes++;
    }

    cout << docked_planes << endl; // Output the maximum number of planes docked

    return 0;
}