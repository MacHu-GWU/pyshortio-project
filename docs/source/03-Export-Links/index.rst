.. _export-links:

🌟Export to TSV: Unleash Your Short.io Links in Spreadsheets 🚀
==============================================================================


Introduction
------------------------------------------------------------------------------
The PyShortIO library provides a convenient export feature that allows you to export all your Short.io links to a TSV (Tab-Separated Values) file. This feature enables you to:

- Create a local backup of your Short.io links
- Analyze your links outside of the Short.io dashboard
- Quickly locate specific links without logging in to Short.io
- Share link information with team members

The export functionality retrieves all links from your Short.io domain and formats them into a structured TSV document that can be easily viewed and edited in spreadsheet applications.


Usage Example
------------------------------------------------------------------------------
Here's a simple example of how to export all your Short.io links to a TSV file:

.. code-block:: python

   # -*- coding: utf-8 -*-

   from pathlib import Path
   from pyshortio.api import Client

   # Initialize client with your API token
   client = Client(token="your_api_token")

   # Export all links for your domain to TSV format
   hostname = "your-domain.short.gy"
   tsv = client.export_to_tsv(hostname=hostname)

   # Save the TSV content to a file
   path_tsv = Path("export.tsv")
   path_tsv.write_text(tsv)

Example output tsv:

.. dropdown:: export.tsv

    .. literalinclude:: ../../../example/export.tsv
       :language: tsv
       :linenos:


Viewing and Editing Exported Links
------------------------------------------------------------------------------
After exporting your links, you can:

1. Open the TSV file in any text editor to view the raw data
2. Import the TSV file into Google Sheets by using "File > Import > Upload" and selecting "Tab-separated values"
3. Open the TSV file directly in Microsoft Excel
4. Use the data for analysis, reporting, or sharing with team members

The exported TSV file includes key information such as original URLs, shortened URLs, titles, paths, and tags, providing a read-only view that allows you to quickly locate the links you want to use without needing to log in to the Short.io dashboard.


Integration with Other Features
------------------------------------------------------------------------------
The export feature complements the existing sync functionality, allowing you to:

1. Export your current links
2. Make modifications in your spreadsheet application
3. Save as TSV
4. Use the :ref:`sync-tsv` feature to apply your changes back to Short.io

This workflow provides a flexible way to manage your Short.io links using familiar spreadsheet tools.
