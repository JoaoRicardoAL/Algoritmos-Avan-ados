/*
Autor: [João Ricardo de Almeida Lustosa]
Esse código simula um jogo de caça-palavras, onde faz uso da tecnica de backtracking e força bruta para encontrar as palavras, a partir de uma matriz de caracteres e uma lista de palavras.
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

class TrieNo
{
public:
    TrieNo *filhos[26];
    bool isLeaf;

    TrieNo()
    {
        isLeaf = false; // Inicializa o nó como não sendo uma folha
        for (int i = 0; i < 26; i++)
            filhos[i] = nullptr; // Inicializa todos os filhos como nulos
    }
};

/* insere():
Função para inserir uma palavra na trie
Parâmetros:
- raiz: ponteiro para o nó raiz da trie
- chave: a palavra a ser inserida
Retorna: verdadeiro se a palavra foi inserida com sucesso, falso caso contrário
*/
void insere(TrieNo *raiz, const string &chave)
{
    TrieNo *atual = raiz;

    for (char c : chave)
    {
        char lowerC = tolower(c); // Converte o caractere para minúsculo
        if (atual->filhos[lowerC - 'a'] == nullptr)
        {
            TrieNo *novoNo = new TrieNo();

            atual->filhos[lowerC - 'a'] = novoNo; // Cria um novo nó se não existir
        }

        atual = atual->filhos[lowerC - 'a']; // Move para o próximo nó
    }

    atual->isLeaf = true; // Marca o nó como folha (palavra completa)
}

/* liberaTrie():
Função para liberar a memória alocada para a trie
Parâmetros:
- no: ponteiro para o nó atual da trie
Retorna: void
*/
void liberaTrie(TrieNo *no)
{
    if (!no)
        return;
    for (int i = 0; i < 26; i++)
        liberaTrie(no->filhos[i]);
    delete no;
}

/* lerMatriz():
Função para ler uma matriz de caracteres
Paramatros:
- linhas: numero de linhas da matriz
- matriz: referência para a matriz onde os caracteres serão armazenados
*/
void lerMatriz(int linhas, int colunas, vector<vector<char>> &matriz)
{
    for (int i = 0; i < linhas; i++)
    {
        string linha;
        cin >> linha;

        if ((int)linha.size() != colunas)
        {
            cerr << "Erro: linha " << i << " tem tamanho diferente de " << colunas << endl;
            exit(1);
        }

        vector<char> row;
        for (char c : linha)
            row.push_back(tolower(c)); // força minúsculo
        matriz.push_back(row);
    }
}

/*buscaTrie():
Função recursiva para buscar palavras na trie a partir de uma posição específica na matriz
Parâmetros:
- raiz: ponteiro para o nó atual da trie
- grid: referência para a matriz de caracteres
- dirX, dirY: direção do movimento na matriz (pode ser -1, 0 ou 1)
- x, y: posição atual na matriz
- palavraAtual: referência para a string que armazena a palavra atual sendo formada
- palavrasEncontradas: referência para o vetor que armazena as palavras encontradas
Retorna: void
*/
void buscaTrie(TrieNo *raiz, vector<vector<char>> &grid, int dirX, int dirY, int x, int y,
               string &palavraAtual, vector<string> &palavrasEncontradas)
{
    // Se o nó atual é uma folha, adiciona a palavra atual à lista de palavras encontradas
    if (raiz->isLeaf)
    {
        if (find(palavrasEncontradas.begin(), palavrasEncontradas.end(), palavraAtual) == palavrasEncontradas.end())
        {
            palavrasEncontradas.push_back(palavraAtual);
        }
    }

    // Calcula a nova posição (novoX, novoY) com base na direção (dirX, dirY)
    int novoX = x + dirX;
    int novoY = y + dirY;

    // Define os limites da matriz
    int linha = grid.size();
    int coluna = grid[0].size();

    // Verifica se a nova posição está dentro dos limites da matriz
    if (novoX >= 0 && novoX < linha && novoY >= 0 && novoY < coluna)
    {
        char proximoChar = grid[novoX][novoY];
        int idx = proximoChar - 'a';
        if (idx < 0 || idx >= 26)
            return;
        TrieNo *proximoNo = raiz->filhos[proximoChar - 'a'];
        if (proximoNo != nullptr)
        {
            palavraAtual.push_back(proximoChar);
            buscaTrie(proximoNo, grid, dirX, dirY, novoX, novoY, palavraAtual, palavrasEncontradas);
            palavraAtual.pop_back();
        }
    }
}

/* cacaPalavra():
Função para encontrar todas as palavras na matriz usando a trie
Parâmetros:
- grid: referência para a matriz de caracteres
- raiz: ponteiro para o nó raiz da trie
- palavrasEncontradas: referência para o vetor que armazena as palavras encontradas
Retorna: void
*/
void cacaPalavra(vector<vector<char>> &grid, TrieNo *raiz, vector<string> &palavrasEncontradas)
{
    // Verifica se a matriz está vazia
    if (grid.empty() || grid[0].empty())
        return;

    // Define os limites da matriz
    int linhas = grid.size();
    int colunas = grid[0].size();

    // Define os offsets para as 8 direções (horizontal, vertical e diagonal)
    int linhaOffset[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int colunaOffset[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            char charAtual = grid[i][j];
            int index = charAtual - 'a';

            if (raiz->filhos[index] != nullptr)
            {
                for (int k = 0; k < 8; k++)
                {
                    string palavraAtual = "";
                    palavraAtual.push_back(charAtual);
                    buscaTrie(raiz->filhos[index], grid, linhaOffset[k], colunaOffset[k], i, j, palavraAtual, palavrasEncontradas);
                }
            }
        }
    }
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
    lerMatriz(linhas, colunas, grid);

    // Leitura do número de palavras a serem encontradas
    int numPalavras;
    cin >> numPalavras;

    TrieNo *trieRaiz = new TrieNo();
    vector<string> palavrasEncontradas;

    // Insere todas as palavras na trie
    for (int i = 0; i < numPalavras; i++)
    {
        string palavra;
        cin >> palavra;
        insere(trieRaiz, palavra);
    }

    cacaPalavra(grid, trieRaiz, palavrasEncontradas);

    // Ordena as palavras encontradas em ordem alfabética
    sort(palavrasEncontradas.begin(), palavrasEncontradas.end());
    // Exibe as palavras encontradas
    if (!palavrasEncontradas.empty())
    {
        cout << palavrasEncontradas.size() << endl;
        for (string &p : palavrasEncontradas)
        {
            transform(p.begin(), p.end(), p.begin(), ::toupper);
            cout << p << endl;
        }
    }

    liberaTrie(trieRaiz);
    return 0;
}
