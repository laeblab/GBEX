# GBEX - Goodbye Excel: A MetaDataStore and more

### What is this?
Instance of DumData GBEX for the DTU BGI group.  

### Docs (work in progress):
Custom instance changes:
  * Nearly all changes of a custom GBEX instance should be made to "GBEX_app/models"
  * Also the hidden files .env and .env_not_docker may need to be adjusted  

There are a few base models that need to be used:
* Profile in "GBEX_app/models/models.py"
  * This model is used to attach a required "table_settings" json object that is used by the frontend to save personalized user settings
* BaseOption
  * This is a model used to store controlled dictionaries.
  * In a GBEXModelBase model, you can have a foreignkey to a BaseOption model and then it will enable autocomplete, search and create options if you use the widgets
* GBEXModelBase in "GBEX_app/models/models.py"
  * This is an abstract model that most other models should inherit
  * It has the following fields that are required by all frontend displayed models:
    * name: This is intended as a non-editable unique human understandable identifier
    * responsible: A link to the USER that created this object
	* created: automatic field with creation date
	* edited: automatic field with edit date
	* archived: Archived objects are not send to the frontend (still accessible in admin interface)
	* order: This object is used to determine which fields should be displayed and in which order
	* symbol: By default, "name" is generated by using "symbol" and adding a number. E.g. Symbol is "PL", then the first object will be "PL1", second object will be "PL2"
	* col_display_func_dict: Most fields have a great default display function, but sometimes you may want to customize it. Almost always the case for many2many objects
	* widgets: By default django default widgets are used, but you may want to used another, e.g. for autocompletes for foreignkeys using django-autocomplete-light
	* model_kind: Currently this can be:
	   * GBEX_Page: This indicates that this is a frontend item
	   * GBEX_Option: This is for a user controlled dictionary. A GBEX_Page model linked field (foreignkey/manytomany) where the user can add items.
	   * GBEX_Batch: If a GBEX_Page model has batches enabled then this is that model =) 
	* col_html_string: By default the react based frontend will just show a string, but columns in this list will be displayed as HTML e.g. to create hyperlinks
	* col_read_only: By default the GUI will attempt to get an edit widget from the backend, but not for columns in this list. Effectively this means that the frontend can't edit these fields.
	* Warning about setting "Unique=True" on a field:
	  * With field with Unique=True you cant directly use the "Number of new items" feature on the model create page.
	  * If you want Unique=True AND to be able to use the "Number of new items", then you need to edit "GBEXCreateView" in GBEX_app/views.py to check the unique constraint before saving and if it fails then provide a solution, e.g. a function to generate a unique entry. 
* Menus are generated by "links" in GBEX_app/template_tags/tags.py 
  * It uses the "menu_label" attribute of models with "model_kind" == "GBEX_Page"

### Changelog
* (14/07/2020) Archive feature: Implemented so it simply hides archived items on list pages. They can still be linked and found in link searches.
* (14/07/2020) Added User model to the REST API
* (15/07/2020) Added Batch concept

### Todos
Move models col_display_func_dict into helpers.field_to_string for many2many fields
Make a custom thing to check on delete whether object is used in Many-to-many relation and if so, prevent deletion

## Deploy
* Install following packages  
  * libsasl2-dev  
  * libldap2-dev

## Suggestions
* Track individual cell line vials
* Make a master bank table that can only be edited by a subset of users.
