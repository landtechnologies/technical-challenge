from treelib import Tree
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='Run exercise')
parser.add_argument("--mode")
parser.add_argument("CompanyID")

companyId_land_map = {}
companyId_parentId_map = {}
input_arg = None
mode = None
supported_modes = ["from_root", "expand"]


def main():
    global input_arg
    global mode
    cli_args = parser.parse_args()
    if cli_args.CompanyID:
        input_arg = cli_args.CompanyID
    if cli_args.mode:
        mode = cli_args.mode

    with open("./land_ownership.csv") as csv_land:
        next(csv_land)
        for line in csv_land:
            land_id, company_id_land = line[:-1].split(",")
            if company_id_land not in companyId_land_map:
                land_count = 1
                companyId_land_map.update({company_id_land: land_count})
            else:
                companyId_land_map.update({company_id_land: companyId_land_map.get(company_id_land) + 1})

    with open("./company_relations.csv") as csv_company:
        next(csv_company)
        for line in csv_company:
            company_id, name, parent_id = line[:-1].split(",")
            companyId_parentId_map.update({company_id: {"parent": parent_id, "name": name}})

    company_id_hierarchy = []
    input_copy = input_arg
    company_id_hierarchy.append(input_copy)
    if input_copy in companyId_parentId_map:
        while companyId_parentId_map.get(input_copy).get('parent') != '':
            input_copy = companyId_parentId_map.get(input_copy).get('parent')
            company_id_hierarchy.append(input_copy)
    else:
        print("Invalid Company ID passed !!")
        return

    root = company_id_hierarchy[len(company_id_hierarchy) - 1]

    d = defaultdict(list)
    for k, v in companyId_parentId_map.items():
        d[v['parent']].append(k)

    tree_full = Tree()
    tree_full.create_node(root, root, parent=None,
                          data=companyId_land_map.get(root) if companyId_land_map.get(root) is not None else 0)
    company_id_node, tree_items = [root], set([root])
    while company_id_node:
        nxt = company_id_node.pop(0)
        for child in d[nxt]:
            tree_full.create_node(child, child, parent=nxt,
                                  data=companyId_land_map.get(child) if companyId_land_map.get(
                                      child) is not None else 0)
            if child not in tree_items:
                company_id_node.append(child)
                tree_items.add(child)

    get_all_land_parcels(tree_full, root)
    update_display_data(tree_full)

    if mode in supported_modes:
        copy_hierarchy = company_id_hierarchy[:]
        if mode == 'from_root':
            copy_hierarchy.pop(0)
        filtered_tree = Tree(tree_full)
        for item in filtered_tree.nodes.keys():
            for child in filtered_tree.children(item):
                if not filtered_tree.parent(child.identifier).identifier in copy_hierarchy and \
                        tree_full.get_node(child.identifier) is not None:
                    tree_full.remove_node(child.identifier)
    else:
        print('Unexpected mode passed in the arguments. Returning Fully expanded tree !!')
    tree_full.show()


def update_display_data(tree: Tree):
    for item in tree.all_nodes():
        if item.identifier == input_arg and mode == 'from_root':
            land_parcel = ' land parcels ***'
        else:
            land_parcel = ' land parcels'
        item.tag = item.tag + '; ' + companyId_parentId_map.get(item.identifier).get('name') + '; owner of ' + \
                   str(item.data) + land_parcel


def get_all_land_parcels(tree, root):
    if tree.children(root) is None or len(tree.children(root)) == 0:
        return tree.get_node(root).data
    for child in tree.children(root):
        tree.get_node(root).data += get_all_land_parcels(tree, child.identifier)
    return tree.get_node(root).data


if __name__ == '__main__':
    main()
