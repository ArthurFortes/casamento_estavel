def casamento_estavel(listas, A, B):
	"""
	>>> from itertools import product
	>>> A = ['1','2','3']
	>>> B = ['a','b','c']
	>>> rank = dict()
	>>> rank['1'] = (1,2,3)
	>>> rank['2'] = (3,1,2)
	>>> rank['3'] = (2,3,1)
	>>> rank['a'] = (1,2,3)
	>>> rank['b'] = (3,1,2)
	>>> rank['c'] = (1,3,2)
	>>> Alistas = dict(((a, rank[a][b_]), B[b_]) for (a, b_) in product(A, range(0, 6)))
	>>> Blistas = dict(((b, rank[b][a_]), A[a_]) for (b, a_) in product(B, range(0, 6)))
	>>> listas = Alistas
	>>> listas.update(Blistas)
	>>> casamento_estavel(listas, A, B)
	[('1', 'a'), ('2', 'b'), ('3', 'd'), ('4', 'f'), ('5', 'c'), ('6', 'e')]
	"""
	pares = dict((a, (listas[(a, 1)], 1)) for a in A)
	eh_estavel = False 
		while eh_estavel == False:
			eh_estavel = True
			for b in B:
				eh_par = False
				for n in range(1, len(B) + 1):
					a = listas[(b, n)]
					a_partner, a_n = pares[a]
					if a_partner == b:
						if eh_par:
							eh_estavel = False
							pares[a] = (listas[(a, a_n + 1)], a_n + 1)
					else:
						eh_par = True

	return sorted((a, b) for (a, (b, n)) in pares.items())
