#include <unordered_map>
#include <unordered_set>
#include <set>
#include <iostream>
#include <deque>


void add(std::unordered_map<int, std::unordered_set<int>> &grafo, int a, int b) {

    if (grafo.contains(a)) grafo[a].insert(b);
    else grafo.insert({a, {b}});

    if (grafo.contains(b)) grafo[b].insert(a);
    else grafo.insert({b, {a}});

}

int percorrer(std::unordered_map<int, std::unordered_set<int>> &grafo) {

    std::unordered_set<int> visited = {1};
    std::set<int> pilha = {1};

    int quantidade = 0;
    std::unordered_map<int, int> anterior;

    while (!pilha.empty()) {

        int u = *pilha.begin();

        visited.insert(u);

        for (int v : grafo[u]) {
            anterior.insert_or_assign(v, u);

            if (!pilha.contains(v)) {

                if (!visited.contains(v)) pilha.insert(v);
                else if (v != anterior[u]) quantidade++;
            }
        }

                pilha.erase(pilha.begin());

    }

    return quantidade;

}


int main() {


    std::unordered_map<int, std::unordered_set<int>> grafo;
    int n, m;
    std::cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        std::cin >> a >> b;
        add(grafo, a, b);
    }

    std::cout << percorrer(grafo);


}