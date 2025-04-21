🌟Sync TSV: The Power Tool for URL Management at Scale 🚀
==============================================================================


Introduction
------------------------------------------------------------------------------
Managing dozens, hundreds, or even thousands of shortened URLs can quickly become overwhelming. That's where PyShortIO's Sync TSV feature comes in - a powerful tool that lets you manage your Short.io links in bulk using simple spreadsheets. This document will showcase how this feature can revolutionize your URL management workflow and provide step-by-step guidance on how to use it effectively.


What is Sync TSV? 🤔
------------------------------------------------------------------------------
Sync TSV is a specialized feature of `PyShortIO <https://github.com/MacHu-GWU/pyshortio-project>`_ that allows you to:

- Create multiple shortened links in one operation
- Update existing links in bulk
- Delete links no longer needed
- Organize links into folders automatically
- Maintain a single source of truth for all your shortened URLs

Think of it as a synchronization bridge between your local data (in a TSV file) and your Short.io account.


TSV File Format 📊
------------------------------------------------------------------------------
A TSV (Tab-Separated Values) file defines all the links you want to manage. Each row represents a link with its properties:

.. dropdown:: example.tsv

    .. literalinclude:: ../../../example/links1.tsv
       :language: csv
       :linenos:


Using Google Sheets as Your TSV Editor
------------------------------------------------------------------------------
For convenient editing and collaboration, you can use Google Sheets as your TSV editor:

`Example Short.io Links Template <https://docs.google.com/spreadsheets/d/1dm6T1Et061wb14iI4m0P9FbQrwb-JQCZGub6e51rK9w/edit?usp=sharing>`_

To use this template:

1. Click the link above to open the example spreadsheet
2. Make a copy for your own use (File > Make a copy)
3. Edit your link data in the spreadsheet
4. When ready to sync, Just select all and copy paste it to a ``.tsv`` file.
5. Use the ``.tsv`` file with the :meth:`~pyshortio.sync_tsv.SyncTSVMixin.sync_tsv` method

This approach makes it easy to collaborate with team members on link management while maintaining a structured format for PyShortIO.


Getting Started with Sync TSV 🚀
------------------------------------------------------------------------------
**Step 1: Create a Simple TSV File**

Create your first TSV file (links1.tsv) with a few links:

.. dropdown:: links1.tsv

    .. literalinclude:: ../../../example/links1.tsv
       :language: csv
       :linenos:

**Step 2: Run Your First Sync**

.. code-block:: python

    # Install with sync dependencies
    # pip install pyshortio[sync]
    from pathlib import Path
    import pyshortio.api as pyshortio

    # Initialize client with your API token
    client = pyshortio.Client(token="your_api_token")

    # Your short.io domain
    hostname = "yourdomain.short.gy"

    # Sync from TSV file
    with open("links1.tsv", "r") as file:
        client.sync_tsv(
            hostname=hostname,
            file=file,
            update_if_not_the_same=True,
            delete_if_not_in_file=False, # Set to True to delete links not in the TSV file
            real_run=True,
        )

The output log would looks like this:

.. dropdown:: log1.txt

    .. literalinclude:: ../../../example/log1.txt
       :language: csv
       :linenos:

**Step 3: Verify Your Links in Short.io**

Log into your Short.io account and confirm that your links have been created successfully.


Understanding the Sync Process 🔄
------------------------------------------------------------------------------
When you run ``sync_tsv()``, PyShortIO follows these steps:

1. Read TSV Data: Parses your TSV file into a structured format
2. Create Folders: Ensures all needed folders exist in your Short.io account
3. Identify Changes: Compares TSV data with existing Short.io links
4. Apply Changes: Creates, updates, and/or deletes links as needed


Incremental Updates with Sync TSV 📈
------------------------------------------------------------------------------
One of the most powerful aspects of Sync TSV is the ability to make incremental updates. Let's see how to update our links with a new TSV file (links2.tsv):

.. dropdown:: links2.tsv

    .. literalinclude:: ../../../example/links2.tsv
       :language: csv
       :linenos:

.. code-block:: python

    # Second sync with updated TSV file
    with open("links2.tsv", "r") as file:
        client.sync_tsv(
            hostname=hostname,
            file=file,
            update_if_not_the_same=True,
            delete_if_not_in_file=True,
            real_run=True,
        )

The output log would looks like this:

.. dropdown:: log2.txt

    .. literalinclude:: ../../../example/log2.txt
       :language: csv
       :linenos:


Understanding Sync Parameters ⚙️
------------------------------------------------------------------------------
- ``hostname``: Your Short.io domain
- ``file``: TSV file containing link data
- ``update_if_not_the_same`` (default: True): Update links that have changed
- ``delete_if_not_in_file`` (default: False): Delete links not present in TSV file
- ``real_run`` (default: True): Actually apply changes (set to False for dry-run)


Advanced Use Cases 🔥
------------------------------------------------------------------------------


Dry Run Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before applying changes to your production domain, run in dry-run mode:

.. code-block:: python

    client.sync_tsv(
        hostname=hostname,
        file=file,
        real_run=False,  # Simulate changes without applying them
    )


Automated Link Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Incorporate Sync TSV into your automated workflows:

.. code-block:: python

    # Example: Daily sync job
    def daily_link_sync():
        # Generate TSV from your database
        generate_tsv_from_database()

        # Sync to Short.io
        with open("generated_links.tsv", "r") as file:
            client.sync_tsv(
                hostname=hostname,
                file=file,
                update_if_not_the_same=True,
                delete_if_not_in_file=True,
            )


Best Practices 🌟
------------------------------------------------------------------------------
- Start with Dry Runs: Use ``real_run=False`` to preview changes before applying them
- Incremental Mode: Set ``delete_if_not_in_file=False`` to only add/update links
- Full Sync Mode: Set ``delete_if_not_in_file=True`` to fully synchronize, removing links not in the TSV
- Version Control Your TSVs: Keep TSV files in Git for history tracking
- Incremental Updates: Start with ``delete_if_not_in_file=False`` until you're comfortable
- Folder Organization: Use the folder_name column to keep links organized
- Automated Testing: Validate your TSV files before syncing


Troubleshooting 🔧
------------------------------------------------------------------------------
**Common Issues**

- Missing Required Columns: Ensure your TSV has at least the original_url column
- Duplicate URLs: Each original URL must be unique in your TSV
- Permission Errors: Verify your API token has write permissions
- Folder Creation Failures: Ensure folder names are valid


Reading Logs
------------------------------------------------------------------------------
The sync process produces detailed logs that can help identify issues:

- 🟢 indicates links to be created
- 🟡 indicates links to be updated
- 🔴 indicates links to be deleted


Conclusion
------------------------------------------------------------------------------
Sync TSV transforms how you manage shortened URLs at scale. Whether you're managing marketing campaigns with dozens of tracking links or maintaining a knowledge base with hundreds of references, this feature makes bulk URL management simple, reliable, and efficient.

Get started today with PyShortIO and leave manual link management behind! 🚀
