using System;

class Program
{
    // Function to find the root of a gate with path compression
    static int Find(int[] parent, int x)
    {
        if (parent[x] != x)
        {
            parent[x] = Find(parent, parent[x]); // Path compression
        }
        return parent[x];
    }

    // Function to union two gates
    static void Union(int[] parent, int x, int y)
    {
        int rootX = Find(parent, x);
        int rootY = Find(parent, y);
        parent[rootX] = rootY; // Union by setting root of x to root of y
    }

    static void Main()
    {
        int G = int.Parse(Console.ReadLine()); // Read number of gates
        int P = int.Parse(Console.ReadLine()); // Read number of planes

        int[] parent = new int[G + 1];
        
        for (int i = 1; i <= G; ++i)
        {
            parent[i] = i; // Initialize each gate to point to itself
        }

        int dockedPlanes = 0;

        for (int i = 0; i < P; ++i)
        {
            int gi = int.Parse(Console.ReadLine()); // Read the preferred gate for each plane
            
            // Find the highest available gate for docking
            int availableGate = Find(parent, gi);

            if (availableGate == 0)
            {
                break; // If no gate is available, stop processing further planes
            }

            // Dock the plane and update the availability of gates
            Union(parent, availableGate, availableGate - 1);
            dockedPlanes++;
        }

        Console.WriteLine(dockedPlanes); // Output the maximum number of planes docked
    }
}