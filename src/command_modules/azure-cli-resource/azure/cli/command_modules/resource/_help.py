# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long
helps['policy'] = """
    type: group
    short-summary: Manage resource policies.
"""
helps['policy definition'] = """
    type: group
    short-summary: Manage resource policy definitions.
"""
helps['policy definition create'] = """
            type: command
            short-summary: Create a policy definition.
            parameters:
                - name: --rules
                  type: string
                  short-summary: 'JSON formatted string or a path to a file with such content'
            examples:
                - name: Create a policy with following rules
                  text: |
                        {
                            "if":
                            {
                                "source": "action",
                                "equals": "Microsoft.Storage/storageAccounts/write"
                            },
                            "then":
                            {
                                "effect": "deny"
                            }
                        }
            """
helps['policy definition delete'] = """
    type: command
    short-summary: Delete a policy definition.
"""
helps['policy definition update'] = """
    type: command
    short-summary: Update a policy definition.
"""
helps['policy definition list'] = """
    type: command
    short-summary: List policy definitions.
"""
helps['policy assignment'] = """
    type: group
    short-summary: Manage resource policy assignments.
"""
helps['policy assignment create'] = """
    type: command
    short-summary: Create a resource policy assignment.
"""
helps['policy assignment delete'] = """
    type: command
    short-summary: Delete a resource policy assignment.
"""
helps['policy assignment show'] = """
    type: command
    short-summary: Show a resource policy assignment.
"""
helps['policy assignment list'] = """
    type: command
    short-summary: list resource policy assignments.
"""
helps['resource'] = """
    type: group
    short-summary: Manage Azure resources.
"""
helps['resource list'] = """
    type: command
    short-summary: List resources.
    examples:
        - name: List all resource in a region.
          text: >
            az resource list --location westus
        - name: List resource using a name.
          text: >
            az resource list --name thename
        - name: List resources using a tag.
          text: >
             az resource list --tag something
        - name: List resources using a tag with a particular prefix.
          text: >
            az resource list --tag some*
        - name: List resources using a tag value.
          text: >
            az resource list --tag something=else
"""

helps['resource show'] = """
    type: command
    short-summary: Get information about a resource.
    long-summary: For example /subscriptions/0000/resourceGroups/MyResourceGroup/providers/Microsoft.Provider/ResA/MyA/ResB/MyB/resC/MyC.
    examples:
        - name: Show a virtual machine.
          text: >
            az vm show -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
        - name: Show a web app using a resource identifier.
          text: >
            az resource show --id /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
        - name: Show a subnet.
          text: >
            az resource show -g MyResourceGroup -n MySubnet --namespace microsoft.network --parent virtualnetworks/MyVnet --resource-type subnets
        - name: Show a subnet using a resource identifier.
          text: >
            az resource show --id /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet
        - name: Show an application gateway path rule.
          text: >
            az resource show -g MyResourceGroup --namespace Microsoft.Network --parent applicationGateways/ag1/urlPathMaps/map1 --resource-type pathRules -n rule1  
"""

helps['resource delete'] = """
    type: command
    short-summary: Delete a resource. Reference the examples for help with arguments.
    long-summary: For example, /subscriptions/0000/resourceGroups/MyResourceGroup/providers/Microsoft.Provider/ResA/MyA/ResB/MyB/ResC/MyC.
    examples:
        - name: Delete a virtual machine.
          text: >
            az vm delete -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
        - name: Delete a web app using a resource identifier.
          text: >
            az resource delete --id /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
        - name: Delete a subnet using a resource identifier.
          text: >
            az resource delete --id /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet
"""

helps['resource tag'] = """
    type: command
    short-summary: Tag a resource. Reference the examples for help with arguments.
    long-summary: For example, /subscriptions/0000/resourceGroups/MyResourceGroup/providers/Microsoft.Provider/ResA/MyA/ResB/MyB/resC/MyC.
    examples:
        - name: Tag a virtual machine.
          text: >
            az resource tag --tags vmlist=vm1 -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"
        - name: Tag a web app using a resource identifier.
          text: >
            az resource tag --tags vmlist=vm1 --id /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
"""

helps['resource update'] = """
    type: command
    short-summary: Update a resource.
"""

helps['feature'] = """
    type: group
    short-summary: Manage resource provider features, such as previews.
"""

helps['group'] = """
    type: group
    short-summary: Manage resource groups.
"""

helps['group exists'] = """
    type: command
    short-summary: Checks whether resource group exists.
    examples:
        - name: Check group existence.
          text: >
            az group exists -n MyResourceGroup
"""

helps['group create'] = """
    type: command
    short-summary: Create a new resource group.
    examples:
        - name: Create a resource group in West US.
          text: >
            az group create -l westus -n MyResourceGroup
"""

helps['group delete'] = """
    type: command
    short-summary: Delete resource group.
    examples:
        - name: Delete a resource group.
          text: >
            az group delete -n MyResourceGroup
"""

helps['group list'] = """
    type: command
    short-summary: List resource groups, optionally filtered by a tag.
    examples:
        - name: List all resource groups for West US.
          text: >
            az group list --query "[?location=='westus']"
"""

helps['group update'] = """
    type: command
    short-summary: Update a resource group.
"""
helps['group wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the resource group is met.
"""
helps['group deployment'] = """
    type: group
    short-summary: Manage Azure Resource Manager deployments.
"""
helps['group deployment create'] = """
    type: command
    short-summary: Start a deployment.
    examples:
        - name: Create a deployment from a remote template file.
          text: >
            az group deployment create -g MyResourceGroup --template-uri https://myresource/azuredeploy.json --parameters @myparameters.json
        - name: Create a deployment from a local template file and use parameter values in a string. 
          text: >
            az group deployment create -g MyResourceGroup --template-file azuredeploy.json --parameters "{\\"location\\": {\\"value\\": \\"westus\\"}}"
"""
helps['group deployment export'] = """
    type: command
    short-summary: Export the template used for the specified deployment.
"""
helps['group deployment validate'] = """
    type: command
    short-summary: Validate whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.
"""
helps['group deployment wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the deployment is met.
"""
helps['group deployment operation'] = """
    type: group
    short-summary: Manage deployment operations.
"""
helps['provider'] = """
    type: group
    short-summary: Manage resource providers.
"""
helps['provider register'] = """
    type: command
    short-summary: Register a provider.
"""
helps['provider unregister'] = """
    type: command
    short-summary: Unregister a provider.
"""
helps['tag'] = """
    type: group
    short-summary: Manage resource tags.
"""
