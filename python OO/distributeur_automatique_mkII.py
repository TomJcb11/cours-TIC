liste_de_fournitures = {
    1: {"name": "Coca-Cola", "unitPrice": 1.5, "quantity": 10},
    2: {"name": "Ice-Tea", "unitPrice": 2, "quantity": 5},
    3: {"name": "Fanta", "unitPrice": 2.5, "quantity": 20},
    4: {"name": "Sprite", "unitPrice": 2.5, "quantity": 15},
    5: {"name": "Orangina", "unitPrice": 2.5, "quantity": 10},
    6: {"name": "Eau", "unitPrice": 1, "quantity": 0},
}
tableau_de_reduction = {
    3: 0.7,  # 30% de réduction pour 3 articles
    4: 0.6,  # 40% de réduction pour 4 articles
}
commmande = {}
action = None
total = 0

print(" \n Bienvenue dans notre magasin, voici nos produits: \n")
for index, details in liste_de_fournitures.items():
    item = details["name"]
    price = details["unitPrice"]
    quantity = details["quantity"]
    print(f"{index}. Produit: {item}, Prix: {price}€, Stock: {quantity}")


def update_unit_price(quantity, price, reductions, reversed=False):
    print(
        "quantity",
        quantity,
        "\n price",
        price,
        "\n reductions",
        reductions,
        "\n reversed",
        reversed,
    )

    for qty, reduction in sorted(reductions.items(), reverse=True):
        if quantity >= qty:
            if reversed:
                return round(price / reduction, 2)
            else:
                return round(price * reduction, 2)
    return round(
        price, 2
    )  # Retourner le prix d'origine si aucune réduction ne s'applique


while action != "q":
    action = input(
        "\n si un de ces produits vous intéresse, veuillez : \n - entrer le numéro du produit que vous souhaitez acheter \n - panier pour consulter/gérer votre panier \n - q pour quitter \n"
    )
    if action.isdigit():
        index = int(action)
        if index in liste_de_fournitures:
            details = liste_de_fournitures[index]
            item = details["name"]
            price = details["unitPrice"]
            quantity = details["quantity"]
            if quantity > 0:
                qty_to_add = input(
                    f" \n Combien de {item} voulez-vous ajouter à votre panier ? (max {quantity}) \n"
                )
                if qty_to_add.isdigit():
                    qty_to_add = int(qty_to_add)
                    if 0 < qty_to_add <= quantity:
                        if item in commmande:
                            commmande[item][1] += qty_to_add
                        else:
                            commmande[item] = [price, qty_to_add]
                        liste_de_fournitures[index]["quantity"] -= qty_to_add
                        updated_price = update_unit_price(
                            commmande[item][1], price, tableau_de_reduction
                        )
                        commmande[item][0] = updated_price
                        total = sum(
                            round(commmande[item][0] * commmande[item][1], 2)
                            for item in commmande
                        )
                        print(
                            f" \n Vous avez ajouté {qty_to_add} {item} pour {round(updated_price * qty_to_add, 2)}€ à votre panier. \n pour consulter votre panier, veuillez entrer 'panier' \n \n"
                        )
                    else:
                        print(" \n Quantité invalide.")
                else:
                    print(" \n Entrée invalide.")
            else:
                print(f" \n Désolé, {item} est en rupture de stock.")
        else:
            print(" \n Numéro de produit invalide.")
    elif action.lower() == "panier":
        if len(commmande) == 0:
            print(" \n Votre panier est vide.")
        else:
            print(" \n Votre panier contient :")
            panier_items = list(commmande.items())
            for index, (item, (price, quantity)) in enumerate(panier_items, start=1):
                print(f"{index}. Produit: {item}, Prix: {price}€, Quantité: {quantity}")
            total = sum(
                round(commmande[item][0] * commmande[item][1], 2) for item in commmande
            )
            print(f"Total: {total}€")

            item_index = input(
                " \n Entrez le numéro du produit que vous voulez supprimer de votre panier : \n"
            )
            if item_index.isdigit():
                item_index = int(item_index) - 1
                if 0 <= item_index < len(panier_items):
                    item, (price, quantity) = panier_items[item_index]
                    if quantity > 1:
                        qty_to_remove = input(
                            f" \n Combien de {item} voulez-vous supprimer ? (max {quantity}) \n"
                        )
                        if qty_to_remove.isdigit():
                            qty_to_remove = int(qty_to_remove)
                            if 0 < qty_to_remove <= quantity:
                                original_price = liste_de_fournitures[
                                    [
                                        k
                                        for k, v in liste_de_fournitures.items()
                                        if v["name"] == item
                                    ][0]
                                ]["unitPrice"]
                                updated_price = update_unit_price(
                                    commmande[item][1] - qty_to_remove,
                                    original_price,
                                    tableau_de_reduction,
                                )
                                total -= round(updated_price * qty_to_remove, 2)
                                liste_de_fournitures[
                                    [
                                        k
                                        for k, v in liste_de_fournitures.items()
                                        if v["name"] == item
                                    ][0]
                                ]["quantity"] += qty_to_remove
                                commmande[item][1] -= qty_to_remove
                                if commmande[item][1] == 0:
                                    del commmande[item]
                                else:
                                    commmande[item][0] = update_unit_price(
                                        commmande[item][1],
                                        original_price,
                                        tableau_de_reduction,
                                    )
                                total = sum(
                                    round(commmande[item][0] * commmande[item][1], 2)
                                    for item in commmande
                                )
                                print(
                                    f" \n {qty_to_remove} {item} ont été supprimés de votre panier."
                                )
                            else:
                                print(" \n Quantité invalide.")
                        else:
                            print(" \n Entrée invalide.")
                    else:
                        total -= round(price * quantity, 2)
                        liste_de_fournitures[
                            [
                                k
                                for k, v in liste_de_fournitures.items()
                                if v["name"] == item
                            ][0]
                        ]["quantity"] += quantity
                        del commmande[item]
                        total = sum(
                            round(commmande[item][0] * commmande[item][1], 2)
                            for item in commmande
                        )
                        print(f" \n {item} a été supprimé de votre panier.")
                else:
                    print(" \n Numéro de produit invalide.")
            else:
                print(" \n Entrée invalide.")
    elif action.lower() == "q":
        print(" \n Merci de votre visite !")
    else:
        print(" \n Commande non reconnue.")
