.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.1 (2025-04-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Added powerful ``pyshortio.api.Client.sync_tsv`` feature for bulk URL management:
    - Create, update, and delete multiple links in one operation
    - Organize links into folders automatically
    - Maintain a single source of truth for all shortened URLs
    - Support for dry run mode with ``real_run=False``
    - Comprehensive logging for tracking changes
- Added ``pyshortio.api.Client.create_folder`` method to create organizational folders:


0.1.1 (2025-04-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add the following API:
    - ``pyshortio.api.Client.list_domains``
    - ``pyshortio.api.Client.get_domain``
    - ``pyshortio.api.Client.get_domain_by_hostname``
    - ``pyshortio.api.Client.list_links``
    - ``pyshortio.api.Client.pagi_list_links``
    - ``pyshortio.api.Client.get_link_opengraph_properties``
    - ``pyshortio.api.Client.get_link_info_by_link_id``
    - ``pyshortio.api.Client.get_link_info_by_path``
    - ``pyshortio.api.Client.list_links_by_original_url``
    - ``pyshortio.api.Client.list_folders``
    - ``pyshortio.api.Client.get_folder``
    - ``pyshortio.api.Client.create_link``
    - ``pyshortio.api.Client.batch_create_links``
    - ``pyshortio.api.Client.update_link``
    - ``pyshortio.api.Client.delete_link``
    - ``pyshortio.api.Client.batch_delete_links``
