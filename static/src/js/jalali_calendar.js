odoo.define("jalali_calendar_crm.jalali_calendar", function (require) {
	"use strict";

	var core = require("web.core");
	var time = require("web.time");
	var field_registry = require("web.field_registry");
	var FieldDate = field_registry.get("date");

	var JalaliCalendarWidget = FieldDate.extend({
		init: function () {
			this._super.apply(this, arguments);
			this.formatOptions.format = time.getLangDateFormat();
		},
		_renderEdit: function () {
			this._super.apply(this, arguments);
			var self = this;
			this.$el.datepicker({
				dateFormat: "yy/mm/dd",
				regional: "fa",
				changeYear: true,
				yearRange: "-100:+0",
				changeMonth: true,
			});
		},
	});

	field_registry.add("jalali_calendar", JalaliCalendarWidget);

	return {
		JalaliCalendarWidget: JalaliCalendarWidget,
	};
});
