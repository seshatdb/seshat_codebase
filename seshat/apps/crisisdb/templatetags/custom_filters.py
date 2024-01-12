from django import template
import re

register = template.Library()


@register.filter
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def get_columns_with_value(instance, value):
    return instance.get_columns_with_value(value)

@register.filter
def get_columns_with_value_dic(instance, value):
    return instance.get_columns_with_value_dic(value)

@register.filter
def replace_underscore_and_capitalize(value):
    value = value.replace('_', ' ')
    return value.title()

@register.filter
def get_item_from_dic(dictionary, key):
    return dictionary.get(key)

@register.filter
def unique_descriptions(values):
    unique_set = set()
    result = []
    
    for value in values:
        if value.description and value.description not in unique_set:
            unique_set.add(value.description)
            result.append(value.description)
    
    return result

@register.filter
def min_max_years(values):
    if not values:
        return ""

    min_year = min(value.year_from for value in values)
    max_year = max(value.year_to for value in values)

    return f"{min_year} - {max_year}"

# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <span type="button"  tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation: </b>\1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     #replacement = r'XYZ_\1_XYZ'
#     new_string = re.sub(pattern, replacement, value)
#     return new_string



# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <span type="button" tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation:</b> \1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     # replacement = r'XYZ_\1_XYZ'
#     new_string = re.sub(pattern, replacement, value)
    
#     # Collect all the values that go into the <sup> tag
#     references = re.findall(pattern, value)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red
#     if references:
#         reference_tags = '\n'.join([f'<p style="color: red;">* {reference}</p>' for reference in references])
#         new_string += reference_tags

#     return new_string


# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup class="fs-6 text-secondary">[{ref_num}]
#     </sup>
#     """
#     new_string = value
#     references = re.findall(pattern, value)
    
#     # Dictionary to store unique reference numbers for each reference
#     reference_numbers = {}
    
#     # Assign a unique reference number to each reference in the order they appear
#     for index, reference in enumerate(references):
#         if reference not in reference_numbers:
#             reference_numbers[reference] = len(reference_numbers) + 1
            
#         ref_num = reference_numbers[reference]
#         sup_tag = replacement.format(ref_num=ref_num)
#         new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red

#     if reference_numbers:
#         new_string += "<h6 class='pt-3 pb-0'># Reference(s): </h6>"
#         reference_tags = '\n'.join([f'<p class="p-0 m-0 fs-6 text-secondary">[{ref_num}]: {reference}</p>' for reference, ref_num in reference_numbers.items()])
#         new_string += reference_tags

#     return new_string


# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <a href="#{ref_id}">{ref_num}</a>
#         <span type="button" tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation:</b> \1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     new_string = value
#     references = re.findall(pattern, value)
    
#     # Dictionary to store unique reference numbers and their corresponding unique identifiers
#     reference_data = {}
    
#     # Assign a unique reference number and identifier to each reference in the order they appear
#     for index, reference in enumerate(references):
#         if reference not in reference_data:
#             reference_data[reference] = {
#                 'ref_num': len(reference_data) + 1,
#                 'ref_id': f'ref_{len(reference_data) + 1}'
#             }
        
#         data = reference_data[reference]
#         sup_tag = replacement.format(ref_num=data['ref_num'], ref_id=data['ref_id'])
#         new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red
#     if reference_data:
#         reference_tags = '\n'.join([f'<p id="{data["ref_id"]}" style="color: red;">[{data["ref_num"]}] {reference}</p>' for reference, data in reference_data.items()])
#         new_string += reference_tags

#     return new_string


import uuid

@register.filter
def make_references_look_nicer(value):
    value = value.replace("'", "&rsquo;").replace("\n", "MJD_BNM_NEWLINE_TAG_XYZ")
    pattern = r'§REF§(.*?)§REF§'
    replacement = r"""<sup class="fs-6" id="sup_{ref_id}">
        <a href="#{ref_id}">[{ref_num}]</a>
    </sup>
    """
    new_string = value
    references = re.findall(pattern, value)
    
    # Dictionary to store unique reference numbers and their corresponding unique identifiers
    reference_data = {}
    
    # Assign a unique reference number and identifier to each reference in the order they appear
    for index, reference in enumerate(references):
        if reference not in reference_data:
            ref_num = len(reference_data) + 1
            ref_id = f"ref_{ref_num}_{str(uuid.uuid4())[:8]}"
            reference_data[reference] = {
                'ref_num': ref_num,
                'ref_id': ref_id
            }
        
        data = reference_data[reference]
        sup_tag = replacement.format(ref_num=data['ref_num'], ref_id=data['ref_id'])
        new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
    # Add the collected references at the end of the string in separate <p> tags with the color red
    if reference_data:
        new_string += "<h6 class='pt-1 pb-0 text-secondary'><i class='fa-solid fa-bookmark fa-xs '></i> Reference(s): </h6>"
        reference_tags = '\n'.join([f'<p id="{data["ref_id"]}" class="p-0 m-0 text-teal"><span class="fw-bold">  <a href="#sup_{data["ref_id"]}">[{data["ref_num"]}]</a></span>: <span style="font-size: 14px;">{reference.replace("MJD_BNM_NEWLINE_TAG_XYZ", " ")}</span> </p>' for reference, data in reference_data.items()])
        new_string += reference_tags

    paargraphed_new_str = new_string.replace("MJD_BNM_NEWLINE_TAG_XYZ", "<br>")
    return paargraphed_new_str
