#####################################################
# CENTRO UNIVERSITÁRIO METODISTA iZABELA hENDRIX/BH #
# Curso: CIÊNCIAS DE DADOS                          #
# PROFESSOR: Neylson Crepalde                       #
# ALUNO: Nelson de Campos Nolasco                   #
#####################################################


# Exercício de Programação Funcional e Orientada a Objetos (OO)

                         ####

# Faça um algoritmo que mostre os “n” termos da seqüência de Fibonacci


# cria um vetor de tamanho n  para armazenar os n resultados

n <- 20
fib <- numeric(n)

# Definindo as condições iniciais
# F1 = 0 e F2 = 1
fib[1] <- 0
fib[2] <- 1

# Agora para todo i > 2 
# calculamos Fi = F(i-1) + F(i - 2)
for(i in 3:n){
  fib[i] <- fib[i - 1] + fib[i - 2]
}

# RESULTADO:  [1]    0    1    1    2    3    5    8   13   21   34   55   89  144  233  377  610  987 1597 2584 4181

fib