/*
Autor: [João Ricardo de Almeida Lustosa]
Esse código simula um jogo de caça-palavras, onde faz uso da tecnica de backtracking e força bruta para encontrar as palavras
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/* lerMatriz():
Função para ler uma matriz de caracteres
Paramatros:
- linhas: numero de linhas da matriz
- matriz: referência para a matriz onde os caracteres serão armazenados
*/
void lerMatriz(int linhas, vector<vector<char>> &matriz)
{
    for (int i = 0; i < linhas; i++)
    {
        string linha;
        cin >> linha;
        vector<char> row(linha.begin(), linha.end());
        matriz.push_back(row);
    }
}

/* backtracking():
Função recursiva para encontrar uma palavra em uma matriz de caracteres, dada uma posição inicial e uma direção
Parâmetros:
- grid: a matriz de caracteres onde a palavra será buscada
- palavra: a palavra a ser encontrada
- x, y: coordenadas atuais na matriz
- index: índice atual na palavra que está sendo buscada
- dX, dY: deslocamento na direção atual (horizontal, vertical ou diagonal)
Retorna: verdadeiro se a palavra for encontrada, falso caso contrário
*/
bool backtracking(vector<vector<char>> &grid, string &palavra, int x, int y, int index, int dX, int dY)
{
    // Condição de parada: se o indice for igual ao tamanho da palavra, significa que encontramos a palavra
    if (static_cast<size_t>(index) == palavra.size())
        return true;

    /* Verificação dos limites da matriz
    Se a posição (x, y) estiver fora dos limites da matriz, retorna falso
    Se a posição (x, y) já foi visitada, retorna falso
    Se o caractere na posição (x, y) do grid não estiver na palavra, retorna falso
    */
    int linha = grid.size();
    int coluna = grid[0].size();
    if (x < 0 || x >= linha || y < 0 || y >= coluna || grid[x][y] != palavra[index])
        return false;

    // Calcula a nova posição (novoX, novoY) com base na direção (dX, dY)
    int novoX = x + dX;
    int novoY = y + dY;

    // Chamada recursiva para verificar a próxima posição
    return backtracking(grid, palavra, novoX, novoY, index + 1, dX, dY);
}

/* encontraPalavra():
Função principal para encontrar uma palavra em uma matriz de caracteres
Parâmetros:
- grid: a matriz de caracteres onde a palavra será buscada
- palavra: a palavra a ser encontrada
Retorna: verdadeiro se a palavra for encontrada, falso caso contrário
*/
bool encontraPalavra(vector<vector<char>> &grid, string &palavra)
{
    // Caso palavra vazia, retorna falso
    if (palavra.empty())
        return false;

    // Verifica se a matriz está vazia ou se a primeira linha está vazia
    if (grid.empty() || grid[0].empty())
        return false;

    // Calcula o número de linhas e colunas da matriz
    int linhas = grid.size();
    int colunas = grid[0].size();

    // Explora as 8 direções possíveis (horizontal, vertical e diagonal)
    int linhaOffset[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int colunaOffset[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    // Procura a primeira letra da palavra no grid
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            if (grid[i][j] == palavra[0])
            {
                for (int k = 0; k < 8; k++)
                {
                    // Explora cada direção, para cada direção, calcula o deslocamento
                    int dX = linhaOffset[k];
                    int dY = colunaOffset[k];

                    // Chmada recursiva para verificar se a palavra pode ser encontrada a partir da posição (i, j), na direção (dX, dY)
                    if (backtracking(grid, palavra, i, j, 0, dX, dY))
                    {
                        return true; // Se encontrou a palavra, retorna verdadeiro
                    }
                }
            }
        }
    }
    return false; // Se não encontrou a palavra, retorna falso
}

int main()
{
    // Leitura das dimensões da matriz
    int linhas;
    cin >> linhas;

    int colunas;
    cin >> colunas;

    // Criação da matriz de caracteres
    vector<vector<char>> grid;

    // Lê a matriz de caracteres
    lerMatriz(linhas, grid);

    // Leitura do número de palavras a serem encontradas
    int numPalavras;
    cin >> numPalavras;

    // Processa cada palavra
    vector<string> palavrasEncontradas;
    for (int i = 0; i < numPalavras; i++)
    {
        string palavra;
        cin >> palavra;
        // Verifica se a palavra pode ser encontrada na matriz
        // Se a palavra for encontrada e ainda não estiver na lista de palavras encontradas, adiciona à lista
        if (encontraPalavra(grid, palavra) &&
            find(palavrasEncontradas.begin(), palavrasEncontradas.end(), palavra) == palavrasEncontradas.end())
        {
            palavrasEncontradas.push_back(palavra);
        }
    }

    // Ordena as palavras encontradas em ordem alfabética
    sort(palavrasEncontradas.begin(), palavrasEncontradas.end());
    // Exibe as palavras encontradas
    if (!palavrasEncontradas.empty())
    {
        cout << palavrasEncontradas.size() << endl;
        for (const string &p : palavrasEncontradas)
        {
            cout << p << endl;
        }
    }

    return 0;
}
