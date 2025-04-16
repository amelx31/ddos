Explications :

    sockets = 10000 : Ouvre 10 000 sockets pour épuiser les connexions d’Apache.
    path = "/wp-admin" : Cible un endpoint lourd.
    user_agents : Randomise les en-têtes pour contourner Snort.
    time.sleep(random.uniform(10, 15)) : Ajoute des délais aléatoires pour éviter les détections.
