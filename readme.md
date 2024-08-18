# Odoo CRM Jalali Calendar Plugin

## Overview

The Odoo CRM Jalali Calendar Plugin adds Jalali (Persian) calendar functionality to all sections of Odoo CRM. This plugin allows users to view and input dates using the Jalali calendar system throughout the Odoo CRM application.

## Features

- Adds a Jalali date field to CRM leads and opportunities
- Provides a custom widget for Jalali date input
- Automatically converts Gregorian dates to Jalali dates
- Integrates seamlessly with existing Odoo CRM views

## Requirements

- Odoo 14.0 or later
- Python 3.6 or later
- `jdatetime` Python library

## Installation

1. Ensure that the `jdatetime` library is installed in your Odoo environment:

   ```
   pip install jdatetime
   ```

2. Clone this repository or download the ZIP file and extract it into your Odoo addons directory:

   ```
   git clone https://github.com/mehdiraized/jalali-calendar-odoo.git /path/to/odoo/addons/jalali_calendar_crm
   ```

3. Update the Odoo modules list:

   - Go to Apps menu
   - Click on "Update Apps List"

4. Install the module:
   - Search for "Jalali Calendar for Odoo CRM" in the Apps menu
   - Click "Install"

## Usage

After installation, the Jalali calendar functionality will be available in the CRM module:

1. Navigate to the CRM module in Odoo
2. Open or create a new lead/opportunity
3. You will see a new "Jalali Date" field, which displays the creation date in Jalali format
4. When editing dates, you can use the Jalali calendar widget to select dates

## Customization

You can extend this plugin to add Jalali calendar support to other modules or fields:

1. Extend the desired model in `models/` directory
2. Add computed Jalali date fields as needed
3. Update the views in `views/` directory to display the new Jalali date fields
4. If necessary, create new JS widgets in `static/src/js/` for custom date input

## Support

For issues, feature requests, or questions, please open an issue on the GitHub repository or contact the author.

## Donate

If you find this plugin useful, please consider supporting its development by [buying me a coffee](https://www.buymeacoffee.com/mehdiraized). Your support helps cover the costs of maintaining and improving the plugin, ensuring it remains free and accessible for everyone. Thank you!

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Mehdi Rezaei](https://mehd.ir)

## Acknowledgments

- Thanks to the Odoo community for their excellent documentation and examples
- The `jdatetime` library developers for providing Jalali date conversion utilities
