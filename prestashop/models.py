# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class MetaCore:

    app_label = 'prestashop'


class Log(models.Model):
    date_log = models.DateTimeField()
    subject = models.CharField(max_length=255)
    texte = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = '_log'


class PsAccess(models.Model):
    id_profile = models.IntegerField()
    id_tab = models.IntegerField()
    view = models.IntegerField()
    add = models.IntegerField()
    edit = models.IntegerField()
    delete = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_access'
        unique_together = (('id_profile', 'id_tab'),)


class PsAccessory(models.Model):
    id_product_1 = models.IntegerField()
    id_product_2 = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_accessory'


class PsAddress(models.Model):
    id_address = models.AutoField(primary_key=True)
    id_country = models.IntegerField()
    id_state = models.IntegerField(blank=True, null=True)
    id_customer = models.IntegerField()
    id_manufacturer = models.IntegerField()
    id_supplier = models.IntegerField()
    id_warehouse = models.IntegerField()
    alias = models.CharField(max_length=32)
    company = models.CharField(max_length=64, blank=True, null=True)
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, blank=True, null=True)
    postcode = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=64)
    other = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    phone_mobile = models.CharField(max_length=32, blank=True, null=True)
    vat_number = models.CharField(max_length=32, blank=True, null=True)
    dni = models.CharField(max_length=16, blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    active = models.IntegerField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_address'


class PsAddressFormat(models.Model):
    id_country = models.IntegerField(primary_key=True)
    format = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_address_format'


class PsAdvice(models.Model):
    id_advice = models.AutoField(primary_key=True)
    id_ps_advice = models.IntegerField()
    id_tab = models.IntegerField()
    ids_tab = models.TextField(blank=True, null=True)
    validated = models.IntegerField()
    hide = models.IntegerField()
    location = models.CharField(max_length=6)
    selector = models.CharField(max_length=255, blank=True, null=True)
    start_day = models.IntegerField()
    stop_day = models.IntegerField()
    weight = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_advice'


class PsAdviceLang(models.Model):
    id_advice = models.IntegerField()
    id_lang = models.IntegerField()
    html = models.TextField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_advice_lang'
        unique_together = (('id_advice', 'id_lang'),)


class PsAlias(models.Model):
    id_alias = models.AutoField(primary_key=True)
    alias = models.CharField(unique=True, max_length=255)
    search = models.CharField(max_length=255)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_alias'


class PsAttachment(models.Model):
    id_attachment = models.AutoField(primary_key=True)
    file = models.CharField(max_length=40)
    file_name = models.CharField(max_length=128)
    file_size = models.BigIntegerField()
    mime = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attachment'


class PsAttachmentLang(models.Model):
    id_attachment = models.AutoField(primary_key=True)
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attachment_lang'
        unique_together = (('id_attachment', 'id_lang'),)


class PsAttribute(models.Model):
    id_attribute = models.AutoField(primary_key=True)
    id_attribute_group = models.IntegerField()
    color = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute'


class PsAttributeGroup(models.Model):
    id_attribute_group = models.AutoField(primary_key=True)
    is_color_group = models.IntegerField()
    group_type = models.CharField(max_length=6)
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_group'


class PsAttributeGroupLang(models.Model):
    id_attribute_group = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128)
    public_name = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_group_lang'
        unique_together = (('id_attribute_group', 'id_lang'),)


class PsAttributeGroupShop(models.Model):
    id_attribute_group = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_group_shop'
        unique_together = (('id_attribute_group', 'id_shop'),)


class PsAttributeImpact(models.Model):
    id_attribute_impact = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_attribute = models.IntegerField()
    weight = models.DecimalField(max_digits=20, decimal_places=6)
    price = models.DecimalField(max_digits=17, decimal_places=2)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_impact'
        unique_together = (('id_product', 'id_attribute'),)


class PsAttributeLang(models.Model):
    id_attribute = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_lang'
        unique_together = (('id_attribute', 'id_lang'),)


class PsAttributeShop(models.Model):
    id_attribute = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_attribute_shop'
        unique_together = (('id_attribute', 'id_shop'),)


class PsBadge(models.Model):
    id_badge = models.AutoField(primary_key=True)
    id_ps_badge = models.IntegerField()
    type = models.CharField(max_length=32)
    id_group = models.IntegerField()
    group_position = models.IntegerField()
    scoring = models.IntegerField()
    awb = models.IntegerField(blank=True, null=True)
    validated = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_badge'


class PsBadgeLang(models.Model):
    id_badge = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_badge_lang'
        unique_together = (('id_badge', 'id_lang'),)


class PsCarrier(models.Model):
    id_carrier = models.AutoField(primary_key=True)
    id_reference = models.IntegerField()
    id_tax_rules_group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    deleted = models.IntegerField()
    shipping_handling = models.IntegerField()
    range_behavior = models.IntegerField()
    is_module = models.IntegerField()
    is_free = models.IntegerField()
    shipping_external = models.IntegerField()
    need_range = models.IntegerField()
    external_module_name = models.CharField(max_length=64, blank=True, null=True)
    shipping_method = models.IntegerField()
    position = models.IntegerField()
    max_width = models.IntegerField(blank=True, null=True)
    max_height = models.IntegerField(blank=True, null=True)
    max_depth = models.IntegerField(blank=True, null=True)
    max_weight = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier'


class PsCarrierGroup(models.Model):
    id_carrier = models.IntegerField()
    id_group = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier_group'
        unique_together = (('id_carrier', 'id_group'),)


class PsCarrierLang(models.Model):
    id_carrier = models.IntegerField()
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    delay = models.CharField(max_length=128, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier_lang'
        unique_together = (('id_lang', 'id_shop', 'id_carrier'),)


class PsCarrierShop(models.Model):
    id_carrier = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier_shop'
        unique_together = (('id_carrier', 'id_shop'),)


class PsCarrierTaxRulesGroupShop(models.Model):
    id_carrier = models.IntegerField()
    id_tax_rules_group = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier_tax_rules_group_shop'
        unique_together = (('id_carrier', 'id_tax_rules_group', 'id_shop'),)


class PsCarrierZone(models.Model):
    id_carrier = models.IntegerField()
    id_zone = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_carrier_zone'
        unique_together = (('id_carrier', 'id_zone'),)


class PsCart(models.Model):
    id_cart = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField()
    id_shop = models.IntegerField()
    id_carrier = models.IntegerField()
    delivery_option = models.TextField()
    id_lang = models.IntegerField()
    id_address_delivery = models.IntegerField()
    id_address_invoice = models.IntegerField()
    id_currency = models.IntegerField()
    id_customer = models.IntegerField()
    id_guest = models.IntegerField()
    secure_key = models.CharField(max_length=32)
    recyclable = models.IntegerField()
    gift = models.IntegerField()
    gift_message = models.TextField(blank=True, null=True)
    mobile_theme = models.IntegerField()
    allow_seperated_package = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart'


class PsCartCartRule(models.Model):
    id_cart = models.IntegerField()
    id_cart_rule = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_cart_rule'
        unique_together = (('id_cart', 'id_cart_rule'),)


class PsCartProduct(models.Model):
    id_cart = models.IntegerField()
    id_product = models.IntegerField()
    id_address_delivery = models.IntegerField(blank=True, null=True)
    id_shop = models.IntegerField()
    id_product_attribute = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_product'


class PsCartRule(models.Model):
    id_cart_rule = models.AutoField(primary_key=True)
    id_customer = models.IntegerField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    quantity_per_user = models.IntegerField()
    priority = models.IntegerField()
    partial_use = models.IntegerField()
    code = models.CharField(max_length=254)
    minimum_amount = models.DecimalField(max_digits=17, decimal_places=2)
    minimum_amount_tax = models.IntegerField()
    minimum_amount_currency = models.IntegerField()
    minimum_amount_shipping = models.IntegerField()
    country_restriction = models.IntegerField()
    carrier_restriction = models.IntegerField()
    group_restriction = models.IntegerField()
    cart_rule_restriction = models.IntegerField()
    product_restriction = models.IntegerField()
    shop_restriction = models.IntegerField()
    free_shipping = models.IntegerField()
    reduction_percent = models.DecimalField(max_digits=5, decimal_places=2)
    reduction_amount = models.DecimalField(max_digits=17, decimal_places=2)
    reduction_tax = models.IntegerField()
    reduction_currency = models.IntegerField()
    reduction_product = models.IntegerField()
    gift_product = models.IntegerField()
    gift_product_attribute = models.IntegerField()
    highlight = models.IntegerField()
    active = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule'


class PsCartRuleCarrier(models.Model):
    id_cart_rule = models.IntegerField()
    id_carrier = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_carrier'
        unique_together = (('id_cart_rule', 'id_carrier'),)


class PsCartRuleCombination(models.Model):
    id_cart_rule_1 = models.IntegerField()
    id_cart_rule_2 = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_combination'
        unique_together = (('id_cart_rule_1', 'id_cart_rule_2'),)


class PsCartRuleCountry(models.Model):
    id_cart_rule = models.IntegerField()
    id_country = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_country'
        unique_together = (('id_cart_rule', 'id_country'),)


class PsCartRuleGroup(models.Model):
    id_cart_rule = models.IntegerField()
    id_group = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_group'
        unique_together = (('id_cart_rule', 'id_group'),)


class PsCartRuleLang(models.Model):
    id_cart_rule = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=254)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_lang'
        unique_together = (('id_cart_rule', 'id_lang'),)


class PsCartRuleProductRule(models.Model):
    id_product_rule = models.AutoField(primary_key=True)
    id_product_rule_group = models.IntegerField()
    type = models.CharField(max_length=13)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_product_rule'


class PsCartRuleProductRuleGroup(models.Model):
    id_product_rule_group = models.AutoField(primary_key=True)
    id_cart_rule = models.IntegerField()
    quantity = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_product_rule_group'


class PsCartRuleProductRuleValue(models.Model):
    id_product_rule = models.IntegerField()
    id_item = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_product_rule_value'
        unique_together = (('id_product_rule', 'id_item'),)


class PsCartRuleShop(models.Model):
    id_cart_rule = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cart_rule_shop'
        unique_together = (('id_cart_rule', 'id_shop'),)


class PsCategory(models.Model):
    id_category = models.AutoField(primary_key=True)
    id_parent = models.IntegerField()
    id_shop_default = models.IntegerField()
    level_depth = models.IntegerField()
    nleft = models.IntegerField()
    nright = models.IntegerField()
    active = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    position = models.IntegerField()
    is_root_category = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_category'


class PsCategoryGroup(models.Model):
    id_category = models.IntegerField()
    id_group = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_category_group'
        unique_together = (('id_category', 'id_group'),)


class PsCategoryLang(models.Model):
    id_category = models.IntegerField(primary_key=True)
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    link_rewrite = models.CharField(max_length=128)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_category_lang'
        unique_together = (('id_category', 'id_shop', 'id_lang'),)


class PsCategoryProduct(models.Model):
    id_category = models.IntegerField()
    id_product = models.IntegerField()
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_category_product'
        unique_together = (('id_category', 'id_product'),)


class PsCategoryShop(models.Model):
    id_category = models.IntegerField()
    id_shop = models.IntegerField()
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_category_shop'
        unique_together = (('id_category', 'id_shop'),)


class PsCms(models.Model):
    id_cms = models.AutoField(primary_key=True)
    id_cms_category = models.IntegerField()
    position = models.IntegerField()
    active = models.IntegerField()
    indexation = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms'


class PsCmsBlock(models.Model):
    id_cms_block = models.AutoField(primary_key=True)
    id_cms_category = models.IntegerField()
    location = models.IntegerField()
    position = models.IntegerField()
    display_store = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_block'


class PsCmsBlockLang(models.Model):
    id_cms_block = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=40)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_block_lang'
        unique_together = (('id_cms_block', 'id_lang'),)


class PsCmsBlockPage(models.Model):
    id_cms_block_page = models.AutoField(primary_key=True)
    id_cms_block = models.IntegerField()
    id_cms = models.IntegerField()
    is_category = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_block_page'


class PsCmsBlockShop(models.Model):
    id_cms_block = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_block_shop'
        unique_together = (('id_cms_block', 'id_shop'),)


class PsCmsCategory(models.Model):
    id_cms_category = models.AutoField(primary_key=True)
    id_parent = models.IntegerField()
    level_depth = models.IntegerField()
    active = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_category'


class PsCmsCategoryLang(models.Model):
    id_cms_category = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    link_rewrite = models.CharField(max_length=128)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_category_lang'
        unique_together = (('id_cms_category', 'id_lang'),)


class PsCmsLang(models.Model):
    id_cms = models.IntegerField()
    id_lang = models.IntegerField()
    meta_title = models.CharField(max_length=128)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    link_rewrite = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_lang'
        unique_together = (('id_cms', 'id_lang'),)


class PsCmsShop(models.Model):
    id_cms = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_cms_shop'
        unique_together = (('id_cms', 'id_shop'),)


class PsCompare(models.Model):
    id_compare = models.AutoField(primary_key=True)
    id_customer = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_compare'


class PsCompareProduct(models.Model):
    id_compare = models.IntegerField()
    id_product = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_compare_product'
        unique_together = (('id_compare', 'id_product'),)


class PsCondition(models.Model):
    id_condition = models.AutoField(primary_key=True)
    id_ps_condition = models.IntegerField()
    type = models.CharField(max_length=13)
    request = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    value = models.CharField(max_length=64, blank=True, null=True)
    result = models.CharField(max_length=64, blank=True, null=True)
    calculation_type = models.CharField(max_length=4, blank=True, null=True)
    calculation_detail = models.CharField(max_length=64, blank=True, null=True)
    validated = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_condition'
        unique_together = (('id_condition', 'id_ps_condition'),)


class PsConditionAdvice(models.Model):
    id_condition = models.IntegerField()
    id_advice = models.IntegerField()
    display = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_condition_advice'
        unique_together = (('id_condition', 'id_advice'),)


class PsConditionBadge(models.Model):
    id_condition = models.IntegerField()
    id_badge = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_condition_badge'
        unique_together = (('id_condition', 'id_badge'),)


class PsConfiguration(models.Model):
    id_configuration = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField(blank=True, null=True)
    id_shop = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=254)
    value = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_configuration'


class PsConfigurationKpi(models.Model):
    id_configuration_kpi = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField(blank=True, null=True)
    id_shop = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=32)
    value = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_configuration_kpi'


class PsConfigurationKpiLang(models.Model):
    id_configuration_kpi = models.IntegerField()
    id_lang = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    date_upd = models.DateTimeField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_configuration_kpi_lang'
        unique_together = (('id_configuration_kpi', 'id_lang'),)


class PsConfigurationLang(models.Model):
    id_configuration = models.IntegerField()
    id_lang = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    date_upd = models.DateTimeField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_configuration_lang'
        unique_together = (('id_configuration', 'id_lang'),)


class PsConnections(models.Model):
    id_connections = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField()
    id_shop = models.IntegerField()
    id_guest = models.IntegerField()
    id_page = models.IntegerField()
    ip_address = models.BigIntegerField(blank=True, null=True)
    date_add = models.DateTimeField()
    http_referer = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_connections'


class PsConnectionsPage(models.Model):
    id_connections = models.IntegerField()
    id_page = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_connections_page'
        unique_together = (('id_connections', 'id_page', 'time_start'),)


class PsConnectionsSource(models.Model):
    id_connections_source = models.AutoField(primary_key=True)
    id_connections = models.IntegerField()
    http_referer = models.CharField(max_length=255, blank=True, null=True)
    request_uri = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_connections_source'


class PsContact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128)
    customer_service = models.IntegerField()
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_contact'


class PsContactLang(models.Model):
    id_contact = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_contact_lang'
        unique_together = (('id_contact', 'id_lang'),)


class PsContactShop(models.Model):
    id_contact = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_contact_shop'
        unique_together = (('id_contact', 'id_shop'),)


class PsCountry(models.Model):
    id_country = models.AutoField(primary_key=True)
    id_zone = models.IntegerField()
    id_currency = models.IntegerField()
    iso_code = models.CharField(max_length=3)
    call_prefix = models.IntegerField()
    active = models.IntegerField()
    contains_states = models.IntegerField()
    need_identification_number = models.IntegerField()
    need_zip_code = models.IntegerField()
    zip_code_format = models.CharField(max_length=12)
    display_tax_label = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_country'


class PsCountryLang(models.Model):
    id_country = models.IntegerField(primary_key=True)
    id_lang = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_country_lang'
        unique_together = (('id_country', 'id_lang'),)


class PsCountryShop(models.Model):
    id_country = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_country_shop'
        unique_together = (('id_country', 'id_shop'),)


class PsCurrency(models.Model):
    id_currency = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    iso_code = models.CharField(max_length=3)
    iso_code_num = models.CharField(max_length=3)
    sign = models.CharField(max_length=8)
    blank = models.IntegerField()
    format = models.IntegerField()
    decimals = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=13, decimal_places=6)
    deleted = models.IntegerField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_currency'


class PsCurrencyShop(models.Model):
    id_currency = models.IntegerField()
    id_shop = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=13, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_currency_shop'
        unique_together = (('id_currency', 'id_shop'),)


class PsCustomField(models.Model):
    id_custom_field = models.AutoField(primary_key=True)
    id_custom_field_section = models.ForeignKey('PsCustomFieldSection', db_column='id_custom_field_section')
    id_shop = models.IntegerField()
    key = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    type_settings = models.TextField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    on_order_details = models.IntegerField()
    on_invoice = models.IntegerField()
    active = models.IntegerField()
    position = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field'


class PsCustomFieldLang(models.Model):
    id_custom_field = models.ForeignKey(PsCustomField, db_column='id_custom_field')
    id_lang = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    error_message = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field_lang'
        unique_together = (('id_custom_field', 'id_lang'),)


class PsCustomFieldOption(models.Model):
    id_custom_field_option = models.AutoField(primary_key=True)
    id_custom_field = models.ForeignKey(PsCustomField, db_column='id_custom_field')
    id_shop = models.IntegerField()
    key = models.CharField(max_length=255, blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    position = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field_option'


class PsCustomFieldOptionLang(models.Model):
    id_custom_field_option = models.ForeignKey(PsCustomFieldOption, db_column='id_custom_field_option')
    id_lang = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field_option_lang'
        unique_together = (('id_custom_field_option', 'id_lang'),)


class PsCustomFieldSection(models.Model):
    id_custom_field_section = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    position = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field_section'


class PsCustomFieldSectionLang(models.Model):
    id_custom_field_section = models.ForeignKey(PsCustomFieldSection, db_column='id_custom_field_section')
    id_lang = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_custom_field_section_lang'
        unique_together = (('id_custom_field_section', 'id_lang'),)


class PsCustomer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField()
    id_shop = models.IntegerField()
    id_gender = models.IntegerField()
    id_default_group = models.IntegerField()
    id_lang = models.IntegerField(blank=True, null=True)
    id_risk = models.IntegerField()
    company = models.CharField(max_length=64, blank=True, null=True)
    siret = models.CharField(max_length=14, blank=True, null=True)
    ape = models.CharField(max_length=5, blank=True, null=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    passwd = models.CharField(max_length=32)
    last_passwd_gen = models.DateTimeField()
    birthday = models.DateField(blank=True, null=True)
    newsletter = models.IntegerField()
    ip_registration_newsletter = models.CharField(max_length=15, blank=True, null=True)
    newsletter_date_add = models.DateTimeField(blank=True, null=True)
    optin = models.IntegerField()
    website = models.CharField(max_length=128, blank=True, null=True)
    outstanding_allow_amount = models.DecimalField(max_digits=20, decimal_places=6)
    show_public_prices = models.IntegerField()
    max_payment_days = models.IntegerField()
    secure_key = models.CharField(max_length=32)
    note = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    is_guest = models.IntegerField()
    deleted = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer'

    def __unicode__(self):
        return ' '.join([self.firstname, self.lastname])


class PsCustomerCode(models.Model):
    id_customer = models.IntegerField()
    date_generated = models.DateTimeField()
    software = models.TextField()
    key = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_code'


class PsCustomerCustomFieldValue(models.Model):
    id_customer_custom_field_value = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(PsCustomer, db_column='id_customer')
    id_custom_field = models.ForeignKey(PsCustomField, db_column='id_custom_field')
    id_custom_field_section = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_custom_field_value'


class PsCustomerGroup(models.Model):
    id_customer = models.IntegerField()
    id_group = models.IntegerField(primary_key=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_group'
        unique_together = (('id_customer', 'id_group'),)


class PsCustomerMessage(models.Model):
    id_customer_message = models.AutoField(primary_key=True)
    id_customer_thread = models.IntegerField(blank=True, null=True)
    id_employee = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    file_name = models.CharField(max_length=18, blank=True, null=True)
    ip_address = models.IntegerField(blank=True, null=True)
    user_agent = models.CharField(max_length=128, blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    private = models.IntegerField()
    read = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_message'


class PsCustomerMessageSyncImap(models.Model):
    md5_header = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_message_sync_imap'


class PsCustomerSubscription(models.Model):
    id_customer = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    id_product = models.IntegerField()
    nb_code = models.IntegerField()
    code_allowed = models.CharField(max_length=255)
    relance1 = models.IntegerField()
    relance2 = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_subscription'


class PsCustomerThread(models.Model):
    id_customer_thread = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    id_contact = models.IntegerField()
    id_customer = models.IntegerField(blank=True, null=True)
    id_order = models.IntegerField(blank=True, null=True)
    id_product = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    email = models.CharField(max_length=128)
    token = models.CharField(max_length=12, blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customer_thread'


class PsCustomization(models.Model):
    id_customization = models.AutoField(primary_key=True)
    id_product_attribute = models.IntegerField()
    id_address_delivery = models.IntegerField()
    id_cart = models.IntegerField()
    id_product = models.IntegerField()
    quantity = models.IntegerField()
    quantity_refunded = models.IntegerField()
    quantity_returned = models.IntegerField()
    in_cart = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customization'
        unique_together = (('id_customization', 'id_cart', 'id_product', 'id_address_delivery'),)


class PsCustomizationField(models.Model):
    id_customization_field = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    type = models.IntegerField()
    required = models.IntegerField()
    specificorganisme = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customization_field'


class PsCustomizationFieldLang(models.Model):
    id_customization_field = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customization_field_lang'
        unique_together = (('id_customization_field', 'id_lang'),)


class PsCustomizedData(models.Model):
    id_customization = models.IntegerField()
    type = models.IntegerField()
    index = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_customized_data'
        unique_together = (('id_customization', 'type', 'index'),)


class PsDateRange(models.Model):
    id_date_range = models.AutoField(primary_key=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_date_range'


class PsDelivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    id_shop = models.IntegerField(blank=True, null=True)
    id_shop_group = models.IntegerField(blank=True, null=True)
    id_carrier = models.IntegerField()
    id_range_price = models.IntegerField(blank=True, null=True)
    id_range_weight = models.IntegerField(blank=True, null=True)
    id_zone = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_delivery'


class PsEmployee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    id_profile = models.IntegerField()
    id_lang = models.IntegerField()
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    passwd = models.CharField(max_length=32)
    last_passwd_gen = models.DateTimeField()
    stats_date_from = models.DateField(blank=True, null=True)
    stats_date_to = models.DateField(blank=True, null=True)
    stats_compare_from = models.DateField(blank=True, null=True)
    stats_compare_to = models.DateField(blank=True, null=True)
    stats_compare_option = models.IntegerField()
    preselect_date_range = models.CharField(max_length=32, blank=True, null=True)
    bo_color = models.CharField(max_length=32, blank=True, null=True)
    bo_theme = models.CharField(max_length=32, blank=True, null=True)
    bo_css = models.CharField(max_length=64, blank=True, null=True)
    default_tab = models.IntegerField()
    bo_width = models.IntegerField()
    bo_menu = models.IntegerField()
    active = models.IntegerField()
    optin = models.IntegerField()
    id_last_order = models.IntegerField()
    id_last_customer_message = models.IntegerField()
    id_last_customer = models.IntegerField()
    telephone = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_employee'


class PsEmployeeProduct(models.Model):
    id_employee = models.IntegerField()
    id_product = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_employee_product'


class PsEmployeeShop(models.Model):
    id_employee = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_employee_shop'
        unique_together = (('id_employee', 'id_shop'),)


class PsFeature(models.Model):
    id_feature = models.AutoField(primary_key=True)
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature'


class PsFeatureLang(models.Model):
    id_feature = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature_lang'
        unique_together = (('id_feature', 'id_lang'),)


class PsFeatureProduct(models.Model):
    id_feature = models.IntegerField()
    id_product = models.IntegerField()
    id_feature_value = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature_product'
        unique_together = (('id_feature', 'id_product'),)


class PsFeatureShop(models.Model):
    id_feature = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature_shop'
        unique_together = (('id_feature', 'id_shop'),)


class PsFeatureValue(models.Model):
    id_feature_value = models.AutoField(primary_key=True)
    id_feature = models.IntegerField()
    custom = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature_value'


class PsFeatureValueLang(models.Model):
    id_feature_value = models.IntegerField()
    id_lang = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_feature_value_lang'
        unique_together = (('id_feature_value', 'id_lang'),)


class PsGender(models.Model):
    id_gender = models.AutoField(primary_key=True)
    type = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_gender'


class PsGenderLang(models.Model):
    id_gender = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_gender_lang'
        unique_together = (('id_gender', 'id_lang'),)


class PsGroup(models.Model):
    id_group = models.AutoField(primary_key=True)
    reduction = models.DecimalField(max_digits=17, decimal_places=2)
    price_display_method = models.IntegerField()
    show_prices = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_group'


class PsGroupLang(models.Model):
    id_group = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_group_lang'
        unique_together = (('id_group', 'id_lang'),)


class PsGroupReduction(models.Model):
    id_group_reduction = models.AutoField(primary_key=True)
    id_group = models.IntegerField()
    id_category = models.IntegerField()
    reduction = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_group_reduction'
        unique_together = (('id_group', 'id_category'),)


class PsGroupShop(models.Model):
    id_group = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_group_shop'
        unique_together = (('id_group', 'id_shop'),)


class PsGuest(models.Model):
    id_guest = models.AutoField(primary_key=True)
    id_operating_system = models.IntegerField(blank=True, null=True)
    id_web_browser = models.IntegerField(blank=True, null=True)
    id_customer = models.IntegerField(blank=True, null=True)
    javascript = models.IntegerField(blank=True, null=True)
    screen_resolution_x = models.SmallIntegerField(blank=True, null=True)
    screen_resolution_y = models.SmallIntegerField(blank=True, null=True)
    screen_color = models.IntegerField(blank=True, null=True)
    sun_java = models.IntegerField(blank=True, null=True)
    adobe_flash = models.IntegerField(blank=True, null=True)
    adobe_director = models.IntegerField(blank=True, null=True)
    apple_quicktime = models.IntegerField(blank=True, null=True)
    real_player = models.IntegerField(blank=True, null=True)
    windows_media = models.IntegerField(blank=True, null=True)
    accept_language = models.CharField(max_length=8, blank=True, null=True)
    mobile_theme = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_guest'


class PsHomeslider(models.Model):
    id_homeslider_slides = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_homeslider'
        unique_together = (('id_homeslider_slides', 'id_shop'),)


class PsHomesliderSlides(models.Model):
    id_homeslider_slides = models.AutoField(primary_key=True)
    position = models.IntegerField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_homeslider_slides'


class PsHomesliderSlidesLang(models.Model):
    id_homeslider_slides = models.IntegerField()
    id_lang = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    legend = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_homeslider_slides_lang'
        unique_together = (('id_homeslider_slides', 'id_lang'),)


class PsHook(models.Model):
    id_hook = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    live_edit = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_hook'


class PsHookAlias(models.Model):
    id_hook_alias = models.AutoField(primary_key=True)
    alias = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_hook_alias'


class PsHookModule(models.Model):
    id_module = models.IntegerField()
    id_shop = models.IntegerField()
    id_hook = models.IntegerField()
    position = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_hook_module'
        unique_together = (('id_module', 'id_hook', 'id_shop'),)


class PsHookModuleExceptions(models.Model):
    id_hook_module_exceptions = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_module = models.IntegerField()
    id_hook = models.IntegerField()
    file_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_hook_module_exceptions'


class PsImage(models.Model):
    id_image = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    position = models.SmallIntegerField()
    cover = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_image'
        unique_together = (('id_image', 'id_product', 'cover'),)


class PsImageLang(models.Model):
    id_image = models.IntegerField()
    id_lang = models.IntegerField()
    legend = models.CharField(max_length=128, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_image_lang'
        unique_together = (('id_image', 'id_lang'),)


class PsImageShop(models.Model):
    id_image = models.IntegerField()
    id_shop = models.IntegerField()
    cover = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_image_shop'


class PsImageType(models.Model):
    id_image_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    width = models.IntegerField()
    height = models.IntegerField()
    products = models.IntegerField()
    categories = models.IntegerField()
    manufacturers = models.IntegerField()
    suppliers = models.IntegerField()
    scenes = models.IntegerField()
    stores = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_image_type'


class PsImportMatch(models.Model):
    id_import_match = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    match = models.TextField()
    skip = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_import_match'


class PsInfo(models.Model):
    id_info = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_info'


class PsInfoLang(models.Model):
    id_info = models.AutoField(primary_key=True)
    id_lang = models.IntegerField()
    text = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_info_lang'
        unique_together = (('id_info', 'id_lang'),)


class PsIrcamFormationFile(models.Model):
    id = models.IntegerField(primary_key=True)
    child_id = models.IntegerField()
    name = models.CharField(max_length=255)
    path = models.TextField()
    type = models.CharField(max_length=255)
    last_generated = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_ircam_formation_file'


class PsLang(models.Model):
    id_lang = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    active = models.IntegerField()
    iso_code = models.CharField(max_length=2)
    language_code = models.CharField(max_length=5)
    date_format_lite = models.CharField(max_length=32)
    date_format_full = models.CharField(max_length=32)
    is_rtl = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_lang'


class PsLangShop(models.Model):
    id_lang = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_lang_shop'
        unique_together = (('id_lang', 'id_shop'),)


class PsLayeredCategory(models.Model):
    id_layered_category = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_category = models.IntegerField()
    id_value = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=18)
    position = models.IntegerField()
    filter_type = models.IntegerField()
    filter_show_limit = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_category'


class PsLayeredFilter(models.Model):
    id_layered_filter = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    filters = models.TextField(blank=True, null=True)
    n_categories = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_filter'


class PsLayeredFilterShop(models.Model):
    id_layered_filter = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_filter_shop'
        unique_together = (('id_layered_filter', 'id_shop'),)


class PsLayeredFriendlyUrl(models.Model):
    id_layered_friendly_url = models.AutoField(primary_key=True)
    url_key = models.CharField(max_length=32)
    data = models.CharField(max_length=200)
    id_lang = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_friendly_url'


class PsLayeredIndexableAttributeGroup(models.Model):
    id_attribute_group = models.IntegerField(primary_key=True)
    indexable = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_attribute_group'


class PsLayeredIndexableAttributeGroupLangValue(models.Model):
    id_attribute_group = models.IntegerField()
    id_lang = models.IntegerField()
    url_name = models.CharField(max_length=20, blank=True, null=True)
    meta_title = models.CharField(max_length=20, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_attribute_group_lang_value'
        unique_together = (('id_attribute_group', 'id_lang'),)


class PsLayeredIndexableAttributeLangValue(models.Model):
    id_attribute = models.IntegerField()
    id_lang = models.IntegerField()
    url_name = models.CharField(max_length=20, blank=True, null=True)
    meta_title = models.CharField(max_length=20, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_attribute_lang_value'
        unique_together = (('id_attribute', 'id_lang'),)


class PsLayeredIndexableFeature(models.Model):
    id_feature = models.IntegerField(primary_key=True)
    indexable = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_feature'


class PsLayeredIndexableFeatureLangValue(models.Model):
    id_feature = models.IntegerField()
    id_lang = models.IntegerField()
    url_name = models.CharField(max_length=20)
    meta_title = models.CharField(max_length=20, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_feature_lang_value'
        unique_together = (('id_feature', 'id_lang'),)


class PsLayeredIndexableFeatureValueLangValue(models.Model):
    id_feature_value = models.IntegerField()
    id_lang = models.IntegerField()
    url_name = models.CharField(max_length=20, blank=True, null=True)
    meta_title = models.CharField(max_length=20, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_indexable_feature_value_lang_value'
        unique_together = (('id_feature_value', 'id_lang'),)


class PsLayeredPriceIndex(models.Model):
    id_product = models.IntegerField()
    id_currency = models.IntegerField()
    id_shop = models.IntegerField()
    price_min = models.IntegerField()
    price_max = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_price_index'
        unique_together = (('id_product', 'id_currency', 'id_shop'),)


class PsLayeredProductAttribute(models.Model):
    id_attribute = models.IntegerField()
    id_product = models.IntegerField()
    id_attribute_group = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_layered_product_attribute'


class PsLinksmenutop(models.Model):
    id_linksmenutop = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    new_window = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_linksmenutop'


class PsLinksmenutopLang(models.Model):
    id_linksmenutop = models.IntegerField()
    id_lang = models.IntegerField()
    id_shop = models.IntegerField()
    label = models.CharField(max_length=128)
    link = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_linksmenutop_lang'


class PsLog(models.Model):
    id_log = models.AutoField(primary_key=True)
    severity = models.IntegerField()
    error_code = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    object_type = models.CharField(max_length=32, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    id_employee = models.IntegerField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_log'


class PsMailalertCustomerOos(models.Model):
    id_customer = models.IntegerField()
    customer_email = models.CharField(max_length=128)
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_mailalert_customer_oos'
        unique_together = (('id_customer', 'customer_email', 'id_product', 'id_product_attribute', 'id_shop'),)


class PsManufacturer(models.Model):
    id_manufacturer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_manufacturer'


class PsManufacturerLang(models.Model):
    id_manufacturer = models.IntegerField()
    id_lang = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_manufacturer_lang'
        unique_together = (('id_manufacturer', 'id_lang'),)


class PsManufacturerShop(models.Model):
    id_manufacturer = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_manufacturer_shop'
        unique_together = (('id_manufacturer', 'id_shop'),)


class PsMaxSerial(models.Model):
    serial = models.CharField(max_length=255)
    student = models.IntegerField()
    used = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_max_serial'


class PsMaxStock(models.Model):
    student = models.IntegerField()
    classic = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_max_stock'


class PsMemcachedServers(models.Model):
    id_memcached_server = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=254)
    port = models.IntegerField()
    weight = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_memcached_servers'


class PsMessage(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_cart = models.IntegerField(blank=True, null=True)
    id_customer = models.IntegerField()
    id_employee = models.IntegerField(blank=True, null=True)
    id_order = models.IntegerField()
    message = models.TextField()
    private = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_message'


class PsMessageReaded(models.Model):
    id_message = models.IntegerField()
    id_employee = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_message_readed'
        unique_together = (('id_message', 'id_employee'),)


class PsMeta(models.Model):
    id_meta = models.AutoField(primary_key=True)
    page = models.CharField(unique=True, max_length=64)
    configurable = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_meta'


class PsMetaLang(models.Model):
    id_meta = models.IntegerField()
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    url_rewrite = models.CharField(max_length=254)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_meta_lang'
        unique_together = (('id_meta', 'id_shop', 'id_lang'),)


class PsModule(models.Model):
    id_module = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    active = models.IntegerField()
    version = models.CharField(max_length=8)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module'


class PsModuleAccess(models.Model):
    id_profile = models.IntegerField()
    id_module = models.IntegerField()
    view = models.IntegerField()
    configure = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_access'
        unique_together = (('id_profile', 'id_module'),)


class PsModuleCountry(models.Model):
    id_module = models.IntegerField()
    id_shop = models.IntegerField()
    id_country = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_country'
        unique_together = (('id_module', 'id_shop', 'id_country'),)


class PsModuleCurrency(models.Model):
    id_module = models.IntegerField()
    id_shop = models.IntegerField()
    id_currency = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_currency'
        unique_together = (('id_module', 'id_shop', 'id_currency'),)


class PsModuleGroup(models.Model):
    id_module = models.IntegerField()
    id_shop = models.IntegerField()
    id_group = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_group'
        unique_together = (('id_module', 'id_shop', 'id_group'),)


class PsModulePreference(models.Model):
    id_module_preference = models.AutoField(primary_key=True)
    id_employee = models.IntegerField()
    module = models.CharField(max_length=255)
    interest = models.IntegerField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_preference'
        unique_together = (('id_employee', 'module'),)


class PsModuleShop(models.Model):
    id_module = models.IntegerField()
    id_shop = models.IntegerField()
    enable_device = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_module_shop'
        unique_together = (('id_module', 'id_shop'),)


class PsNewsletter(models.Model):
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    email = models.CharField(max_length=255)
    newsletter_date_add = models.DateTimeField(blank=True, null=True)
    ip_registration_newsletter = models.CharField(max_length=15)
    http_referer = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_newsletter'


class PsOperatingSystem(models.Model):
    id_operating_system = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_operating_system'


class PsOrderCarrier(models.Model):
    id_order_carrier = models.AutoField(primary_key=True)
    id_order = models.IntegerField()
    id_carrier = models.IntegerField()
    id_order_invoice = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    shipping_cost_tax_excl = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    shipping_cost_tax_incl = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    tracking_number = models.CharField(max_length=64, blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_carrier'


class PsOrderCartRule(models.Model):
    id_order_cart_rule = models.AutoField(primary_key=True)
    id_order = models.IntegerField()
    id_cart_rule = models.IntegerField()
    id_order_invoice = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=254)
    value = models.DecimalField(max_digits=17, decimal_places=2)
    value_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    free_shipping = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_cart_rule'


class PsOrderDetail(models.Model):
    id_order_detail = models.AutoField(primary_key=True)
    id_order = models.IntegerField()
    id_order_invoice = models.IntegerField(blank=True, null=True)
    id_warehouse = models.IntegerField(blank=True, null=True)
    id_shop = models.IntegerField()
    product_id = models.IntegerField()
    product_attribute_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    product_quantity_in_stock = models.IntegerField()
    product_quantity_refunded = models.IntegerField()
    product_quantity_return = models.IntegerField()
    product_quantity_reinjected = models.IntegerField()
    product_price = models.DecimalField(max_digits=20, decimal_places=6)
    reduction_percent = models.DecimalField(max_digits=10, decimal_places=2)
    reduction_amount = models.DecimalField(max_digits=20, decimal_places=6)
    reduction_amount_tax_incl = models.DecimalField(max_digits=20, decimal_places=6)
    reduction_amount_tax_excl = models.DecimalField(max_digits=20, decimal_places=6)
    group_reduction = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity_discount = models.DecimalField(max_digits=20, decimal_places=6)
    product_ean13 = models.CharField(max_length=13, blank=True, null=True)
    product_upc = models.CharField(max_length=12, blank=True, null=True)
    product_reference = models.CharField(max_length=32, blank=True, null=True)
    product_supplier_reference = models.CharField(max_length=32, blank=True, null=True)
    product_weight = models.DecimalField(max_digits=20, decimal_places=6)
    tax_computation_method = models.IntegerField()
    tax_name = models.CharField(max_length=16)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=3)
    ecotax = models.DecimalField(max_digits=21, decimal_places=6)
    ecotax_tax_rate = models.DecimalField(max_digits=5, decimal_places=3)
    discount_quantity_applied = models.IntegerField()
    download_hash = models.CharField(max_length=255, blank=True, null=True)
    download_nb = models.IntegerField(blank=True, null=True)
    download_deadline = models.DateTimeField(blank=True, null=True)
    total_price_tax_incl = models.DecimalField(max_digits=20, decimal_places=6)
    total_price_tax_excl = models.DecimalField(max_digits=20, decimal_places=6)
    unit_price_tax_incl = models.DecimalField(max_digits=20, decimal_places=6)
    unit_price_tax_excl = models.DecimalField(max_digits=20, decimal_places=6)
    total_shipping_price_tax_incl = models.DecimalField(max_digits=20, decimal_places=6)
    total_shipping_price_tax_excl = models.DecimalField(max_digits=20, decimal_places=6)
    purchase_supplier_price = models.DecimalField(max_digits=20, decimal_places=6)
    original_product_price = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_detail'


class PsOrderDetailTax(models.Model):
    id_order_detail = models.IntegerField(primary_key=True)
    id_tax = models.IntegerField()
    unit_amount = models.DecimalField(max_digits=16, decimal_places=6)
    total_amount = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_detail_tax'


class PsOrderHistory(models.Model):
    id_order_history = models.AutoField(primary_key=True)
    id_employee = models.IntegerField()
    id_order = models.IntegerField()
    id_order_state = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_history'


class PsOrderInvoice(models.Model):
    id_order_invoice = models.AutoField(primary_key=True)
    id_order = models.IntegerField()
    number = models.IntegerField()
    delivery_number = models.IntegerField()
    delivery_date = models.DateTimeField(blank=True, null=True)
    total_discount_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_discount_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_products = models.DecimalField(max_digits=17, decimal_places=2)
    total_products_wt = models.DecimalField(max_digits=17, decimal_places=2)
    total_shipping_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_shipping_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    shipping_tax_computation_method = models.IntegerField()
    total_wrapping_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_wrapping_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_invoice'


class PsOrderInvoicePayment(models.Model):
    id_order_invoice = models.IntegerField()
    id_order_payment = models.IntegerField()
    id_order = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_invoice_payment'
        unique_together = (('id_order_invoice', 'id_order_payment'),)


class PsOrderInvoiceTax(models.Model):
    id_order_invoice = models.IntegerField()
    type = models.CharField(max_length=15)
    id_tax = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_invoice_tax'


class PsOrderMessage(models.Model):
    id_order_message = models.AutoField(primary_key=True)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_message'


class PsOrderMessageLang(models.Model):
    id_order_message = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128)
    message = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_message_lang'
        unique_together = (('id_order_message', 'id_lang'),)


class PsOrderPayment(models.Model):
    id_order_payment = models.AutoField(primary_key=True)
    order_reference = models.CharField(max_length=9, blank=True, null=True)
    id_currency = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    conversion_rate = models.DecimalField(max_digits=13, decimal_places=6)
    transaction_id = models.CharField(max_length=254, blank=True, null=True)
    card_number = models.CharField(max_length=254, blank=True, null=True)
    card_brand = models.CharField(max_length=254, blank=True, null=True)
    card_expiration = models.CharField(max_length=7, blank=True, null=True)
    card_holder = models.CharField(max_length=254, blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_payment'


class PsOrderReturn(models.Model):
    id_order_return = models.AutoField(primary_key=True)
    id_customer = models.IntegerField()
    id_order = models.IntegerField()
    state = models.IntegerField()
    question = models.TextField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_return'


class PsOrderReturnDetail(models.Model):
    id_order_return = models.IntegerField()
    id_order_detail = models.IntegerField()
    id_customization = models.IntegerField()
    product_quantity = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_return_detail'
        unique_together = (('id_order_return', 'id_order_detail', 'id_customization'),)


class PsOrderReturnState(models.Model):
    id_order_return_state = models.AutoField(primary_key=True)
    color = models.CharField(max_length=32, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_return_state'


class PsOrderReturnStateLang(models.Model):
    id_order_return_state = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_return_state_lang'
        unique_together = (('id_order_return_state', 'id_lang'),)


class PsOrderSlip(models.Model):
    id_order_slip = models.AutoField(primary_key=True)
    conversion_rate = models.DecimalField(max_digits=13, decimal_places=6)
    id_customer = models.IntegerField()
    id_order = models.IntegerField()
    shipping_cost = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    partial = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_slip'


class PsOrderSlipDetail(models.Model):
    id_order_slip = models.IntegerField()
    id_order_detail = models.IntegerField()
    product_quantity = models.IntegerField()
    amount_tax_excl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_tax_incl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_slip_detail'
        unique_together = (('id_order_slip', 'id_order_detail'),)


class PsOrderState(models.Model):
    id_order_state = models.AutoField(primary_key=True)
    invoice = models.IntegerField(blank=True, null=True)
    send_email = models.IntegerField()
    module_name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    unremovable = models.IntegerField()
    hidden = models.IntegerField()
    logable = models.IntegerField()
    delivery = models.IntegerField()
    shipped = models.IntegerField()
    paid = models.IntegerField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_state'


class PsOrderStateLang(models.Model):
    id_order_state = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=64)
    template = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_order_state_lang'
        unique_together = (('id_order_state', 'id_lang'),)


class PsOrders(models.Model):
    id_order = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=9, blank=True, null=True)
    id_shop_group = models.IntegerField()
    id_shop = models.IntegerField()
    id_carrier = models.IntegerField()
    id_lang = models.IntegerField()
    id_customer = models.IntegerField()
    id_cart = models.IntegerField()
    id_currency = models.IntegerField()
    id_address_delivery = models.IntegerField()
    id_address_invoice = models.IntegerField()
    current_state = models.IntegerField()
    secure_key = models.CharField(max_length=32)
    payment = models.CharField(max_length=255)
    conversion_rate = models.DecimalField(max_digits=13, decimal_places=6)
    module = models.CharField(max_length=255, blank=True, null=True)
    recyclable = models.IntegerField()
    gift = models.IntegerField()
    gift_message = models.TextField(blank=True, null=True)
    mobile_theme = models.IntegerField()
    shipping_number = models.CharField(max_length=32, blank=True, null=True)
    total_discounts = models.DecimalField(max_digits=17, decimal_places=2)
    total_discounts_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_discounts_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    total_paid_real = models.DecimalField(max_digits=17, decimal_places=2)
    total_products = models.DecimalField(max_digits=17, decimal_places=2)
    total_products_wt = models.DecimalField(max_digits=17, decimal_places=2)
    total_shipping = models.DecimalField(max_digits=17, decimal_places=2)
    total_shipping_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_shipping_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    carrier_tax_rate = models.DecimalField(max_digits=10, decimal_places=3)
    total_wrapping = models.DecimalField(max_digits=17, decimal_places=2)
    total_wrapping_tax_incl = models.DecimalField(max_digits=17, decimal_places=2)
    total_wrapping_tax_excl = models.DecimalField(max_digits=17, decimal_places=2)
    invoice_number = models.IntegerField()
    delivery_number = models.IntegerField()
    invoice_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    valid = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    is_organisme = models.IntegerField()
    id_organisme = models.IntegerField()
    export_max = models.IntegerField()
    treated_group = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_orders'


class PsPack(models.Model):
    id_product_pack = models.IntegerField()
    id_product_item = models.IntegerField()
    quantity = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_pack'
        unique_together = (('id_product_pack', 'id_product_item'),)


class PsPage(models.Model):
    id_page = models.AutoField(primary_key=True)
    id_page_type = models.IntegerField()
    id_object = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_page'


class PsPageType(models.Model):
    id_page_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_page_type'


class PsPageViewed(models.Model):
    id_page = models.IntegerField()
    id_shop_group = models.IntegerField()
    id_shop = models.IntegerField()
    id_date_range = models.IntegerField()
    counter = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_page_viewed'
        unique_together = (('id_page', 'id_date_range', 'id_shop'),)


class PsPagenotfound(models.Model):
    id_pagenotfound = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    request_uri = models.CharField(max_length=256)
    http_referer = models.CharField(max_length=256)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_pagenotfound'


class PsPayboxAuthorisedAwaitCapture(models.Model):
    id_authorised = models.AutoField(primary_key=True)
    id_order = models.IntegerField()
    numtrans = models.CharField(max_length=254)
    numappel = models.CharField(max_length=254)
    refabonne = models.CharField(max_length=254, blank=True, null=True)
    coderesponse = models.IntegerField()
    dateq = models.CharField(max_length=254)
    numquestion = models.CharField(max_length=254)
    captured = models.IntegerField()
    amount_paid = models.IntegerField()
    refunded = models.IntegerField()
    amount_refunded = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_paybox_authorised_await_capture'


class PsPayboxContracts(models.Model):
    id_paybox_contract = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    image = models.CharField(max_length=254, blank=True, null=True)
    payment_type = models.CharField(max_length=254, blank=True, null=True)
    card_type = models.CharField(max_length=254, blank=True, null=True)
    active = models.IntegerField()
    paid_shipping = models.IntegerField()
    deferred = models.IntegerField()
    refund = models.IntegerField()
    immediate = models.IntegerField()
    deletable = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_paybox_contracts'


class PsPayboxCustomerIp(models.Model):
    id_client_ip = models.AutoField(primary_key=True)
    client_ip_address = models.CharField(max_length=254, blank=True, null=True)
    id_order = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_paybox_customer_ip'


class PsProduct(models.Model):
    id_product = models.AutoField(primary_key=True)
    id_supplier = models.IntegerField(blank=True, null=True)
    id_manufacturer = models.IntegerField(blank=True, null=True)
    id_category_default = models.IntegerField(blank=True, null=True)
    id_shop_default = models.IntegerField()
    id_tax_rules_group = models.IntegerField()
    on_sale = models.IntegerField()
    online_only = models.IntegerField()
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    upc = models.CharField(max_length=12, blank=True, null=True)
    ecotax = models.DecimalField(max_digits=17, decimal_places=6)
    quantity = models.IntegerField()
    minimal_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=6)
    unity = models.CharField(max_length=255, blank=True, null=True)
    unit_price_ratio = models.DecimalField(max_digits=20, decimal_places=6)
    additional_shipping_cost = models.DecimalField(max_digits=20, decimal_places=2)
    reference = models.CharField(max_length=32, blank=True, null=True)
    supplier_reference = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    width = models.DecimalField(max_digits=20, decimal_places=6)
    height = models.DecimalField(max_digits=20, decimal_places=6)
    depth = models.DecimalField(max_digits=20, decimal_places=6)
    weight = models.DecimalField(max_digits=20, decimal_places=6)
    out_of_stock = models.IntegerField()
    quantity_discount = models.IntegerField(blank=True, null=True)
    customizable = models.IntegerField()
    uploadable_files = models.IntegerField()
    text_fields = models.IntegerField()
    active = models.IntegerField()
    redirect_type = models.CharField(max_length=3)
    id_product_redirected = models.IntegerField()
    available_for_order = models.IntegerField()
    available_date = models.DateField()
    condition = models.CharField(max_length=11)
    show_price = models.IntegerField()
    indexed = models.IntegerField()
    visibility = models.CharField(max_length=7)
    cache_is_pack = models.IntegerField()
    cache_has_attachments = models.IntegerField()
    is_virtual = models.IntegerField()
    cache_default_attribute = models.IntegerField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    advanced_stock_management = models.IntegerField()
    room = models.CharField(max_length=255)
    teachers = models.TextField()
    hotesse = models.TextField()
    teaching_lang = models.CharField(max_length=255)
    mapping = models.TextField()
    available_until_date = models.DateTimeField()
    top = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product'


class PsProductAttachment(models.Model):
    id_product = models.IntegerField()
    id_attachment = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_attachment'
        unique_together = (('id_product', 'id_attachment'),)


class PsProductAttribute(models.Model):
    id_product_attribute = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    reference = models.CharField(max_length=32, blank=True, null=True)
    supplier_reference = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    upc = models.CharField(max_length=12, blank=True, null=True)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=6)
    price = models.DecimalField(max_digits=20, decimal_places=6)
    ecotax = models.DecimalField(max_digits=17, decimal_places=6)
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=20, decimal_places=6)
    unit_price_impact = models.DecimalField(max_digits=17, decimal_places=2)
    default_on = models.IntegerField()
    minimal_quantity = models.IntegerField()
    available_date = models.DateField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_attribute'


class PsProductAttributeCombination(models.Model):
    id_attribute = models.IntegerField()
    id_product_attribute = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_attribute_combination'
        unique_together = (('id_attribute', 'id_product_attribute'),)


class PsProductAttributeImage(models.Model):
    id_product_attribute = models.IntegerField()
    id_image = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_attribute_image'
        unique_together = (('id_product_attribute', 'id_image'),)


class PsProductAttributeShop(models.Model):
    id_product_attribute = models.IntegerField()
    id_shop = models.IntegerField()
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=6)
    price = models.DecimalField(max_digits=20, decimal_places=6)
    ecotax = models.DecimalField(max_digits=17, decimal_places=6)
    weight = models.DecimalField(max_digits=20, decimal_places=6)
    unit_price_impact = models.DecimalField(max_digits=17, decimal_places=2)
    default_on = models.IntegerField()
    minimal_quantity = models.IntegerField()
    available_date = models.DateField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_attribute_shop'
        unique_together = (('id_product_attribute', 'id_shop'),)


class PsProductCarrier(models.Model):
    id_product = models.IntegerField()
    id_carrier_reference = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_carrier'
        unique_together = (('id_product', 'id_carrier_reference', 'id_shop'),)


class PsProductComment(models.Model):
    id_product_comment = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_customer = models.IntegerField()
    id_guest = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    content = models.TextField()
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    grade = models.FloatField()
    validate = models.IntegerField()
    deleted = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment'


class PsProductCommentCriterion(models.Model):
    id_product_comment_criterion = models.AutoField(primary_key=True)
    id_product_comment_criterion_type = models.IntegerField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_criterion'


class PsProductCommentCriterionCategory(models.Model):
    id_product_comment_criterion = models.IntegerField()
    id_category = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_criterion_category'
        unique_together = (('id_product_comment_criterion', 'id_category'),)


class PsProductCommentCriterionLang(models.Model):
    id_product_comment_criterion = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_criterion_lang'
        unique_together = (('id_product_comment_criterion', 'id_lang'),)


class PsProductCommentCriterionProduct(models.Model):
    id_product = models.IntegerField()
    id_product_comment_criterion = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_criterion_product'
        unique_together = (('id_product', 'id_product_comment_criterion'),)


class PsProductCommentGrade(models.Model):
    id_product_comment = models.IntegerField()
    id_product_comment_criterion = models.IntegerField()
    grade = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_grade'
        unique_together = (('id_product_comment', 'id_product_comment_criterion'),)


class PsProductCommentReport(models.Model):
    id_product_comment = models.IntegerField()
    id_customer = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_report'
        unique_together = (('id_product_comment', 'id_customer'),)


class PsProductCommentUsefulness(models.Model):
    id_product_comment = models.IntegerField()
    id_customer = models.IntegerField()
    usefulness = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_comment_usefulness'
        unique_together = (('id_product_comment', 'id_customer'),)


class PsProductCountryTax(models.Model):
    id_product = models.IntegerField()
    id_country = models.IntegerField()
    id_tax = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_country_tax'
        unique_together = (('id_product', 'id_country'),)


class PsProductDownload(models.Model):
    id_product_download = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    display_filename = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    date_add = models.DateTimeField()
    date_expiration = models.DateTimeField(blank=True, null=True)
    nb_days_accessible = models.IntegerField(blank=True, null=True)
    nb_downloadable = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    is_shareable = models.IntegerField()
    release_note = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_download'


class PsProductDownloadStat(models.Model):
    aid_product = models.IntegerField()
    date_download = models.DateTimeField()
    ip_download = models.CharField(max_length=255)
    id_customer = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_download_stat'


class PsProductGroupReductionCache(models.Model):
    id_product = models.IntegerField()
    id_group = models.IntegerField()
    reduction = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_group_reduction_cache'
        unique_together = (('id_product', 'id_group'),)


class PsProductLang(models.Model):
    id_product = models.IntegerField(primary_key=True)
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    description_short = models.TextField(blank=True, null=True)
    link_rewrite = models.CharField(max_length=128)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128)
    available_now = models.CharField(max_length=255, blank=True, null=True)
    available_later = models.CharField(max_length=255, blank=True, null=True)
    dates = models.TextField()
    times = models.TextField()
    length = models.CharField(max_length=255)
    teaching_lang = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_lang'
        unique_together = (('id_product', 'id_shop', 'id_lang'),)


class PsProductSale(models.Model):
    id_product = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    sale_nbr = models.IntegerField()
    date_upd = models.DateField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_sale'


class PsProductShop(models.Model):
    id_product = models.IntegerField()
    id_shop = models.IntegerField()
    id_category_default = models.IntegerField(blank=True, null=True)
    id_tax_rules_group = models.IntegerField()
    on_sale = models.IntegerField()
    online_only = models.IntegerField()
    ecotax = models.DecimalField(max_digits=17, decimal_places=6)
    minimal_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=6)
    unity = models.CharField(max_length=255, blank=True, null=True)
    unit_price_ratio = models.DecimalField(max_digits=20, decimal_places=6)
    additional_shipping_cost = models.DecimalField(max_digits=20, decimal_places=2)
    customizable = models.IntegerField()
    uploadable_files = models.IntegerField()
    text_fields = models.IntegerField()
    active = models.IntegerField()
    redirect_type = models.CharField(max_length=3)
    id_product_redirected = models.IntegerField()
    available_for_order = models.IntegerField()
    available_date = models.DateField()
    condition = models.CharField(max_length=11)
    show_price = models.IntegerField()
    indexed = models.IntegerField()
    visibility = models.CharField(max_length=7)
    cache_default_attribute = models.IntegerField(blank=True, null=True)
    advanced_stock_management = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_shop'
        unique_together = (('id_product', 'id_shop'),)


class PsProductSupplier(models.Model):
    id_product_supplier = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    id_supplier = models.IntegerField()
    product_supplier_reference = models.CharField(max_length=32, blank=True, null=True)
    product_supplier_price_te = models.DecimalField(max_digits=20, decimal_places=6)
    id_currency = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_supplier'
        unique_together = (('id_product', 'id_product_attribute', 'id_supplier'),)


class PsProductTag(models.Model):
    id_product = models.IntegerField()
    id_tag = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_tag'
        unique_together = (('id_product', 'id_tag'),)


class PsProductTeacher(models.Model):
    id_product = models.IntegerField()
    id_teacher = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_product_teacher'


class PsProfile(models.Model):
    id_profile = models.AutoField(primary_key=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_profile'


class PsProfileLang(models.Model):
    id_lang = models.IntegerField()
    id_profile = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_profile_lang'
        unique_together = (('id_profile', 'id_lang'),)


class PsQuickAccess(models.Model):
    id_quick_access = models.AutoField(primary_key=True)
    new_window = models.IntegerField()
    link = models.CharField(max_length=128)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_quick_access'


class PsQuickAccessLang(models.Model):
    id_quick_access = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_quick_access_lang'
        unique_together = (('id_quick_access', 'id_lang'),)


class PsRangePrice(models.Model):
    id_range_price = models.AutoField(primary_key=True)
    id_carrier = models.IntegerField()
    delimiter1 = models.DecimalField(max_digits=20, decimal_places=6)
    delimiter2 = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_range_price'
        unique_together = (('id_carrier', 'delimiter1', 'delimiter2'),)


class PsRangeWeight(models.Model):
    id_range_weight = models.AutoField(primary_key=True)
    id_carrier = models.IntegerField()
    delimiter1 = models.DecimalField(max_digits=20, decimal_places=6)
    delimiter2 = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_range_weight'
        unique_together = (('id_carrier', 'delimiter1', 'delimiter2'),)


class PsReferrer(models.Model):
    id_referrer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    passwd = models.CharField(max_length=32, blank=True, null=True)
    http_referer_regexp = models.CharField(max_length=64, blank=True, null=True)
    http_referer_like = models.CharField(max_length=64, blank=True, null=True)
    request_uri_regexp = models.CharField(max_length=64, blank=True, null=True)
    request_uri_like = models.CharField(max_length=64, blank=True, null=True)
    http_referer_regexp_not = models.CharField(max_length=64, blank=True, null=True)
    http_referer_like_not = models.CharField(max_length=64, blank=True, null=True)
    request_uri_regexp_not = models.CharField(max_length=64, blank=True, null=True)
    request_uri_like_not = models.CharField(max_length=64, blank=True, null=True)
    base_fee = models.DecimalField(max_digits=5, decimal_places=2)
    percent_fee = models.DecimalField(max_digits=5, decimal_places=2)
    click_fee = models.DecimalField(max_digits=5, decimal_places=2)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_referrer'


class PsReferrerCache(models.Model):
    id_connections_source = models.IntegerField()
    id_referrer = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_referrer_cache'
        unique_together = (('id_connections_source', 'id_referrer'),)


class PsReferrerShop(models.Model):
    id_referrer = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    cache_visitors = models.IntegerField(blank=True, null=True)
    cache_visits = models.IntegerField(blank=True, null=True)
    cache_pages = models.IntegerField(blank=True, null=True)
    cache_registrations = models.IntegerField(blank=True, null=True)
    cache_orders = models.IntegerField(blank=True, null=True)
    cache_sales = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    cache_reg_rate = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    cache_order_rate = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_referrer_shop'
        unique_together = (('id_referrer', 'id_shop'),)


class PsRequestSql(models.Model):
    id_request_sql = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sql = models.TextField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_request_sql'


class PsRequiredField(models.Model):
    id_required_field = models.AutoField(primary_key=True)
    object_name = models.CharField(max_length=32)
    field_name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_required_field'


class PsRisk(models.Model):
    id_risk = models.AutoField(primary_key=True)
    percent = models.IntegerField()
    color = models.CharField(max_length=32, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_risk'


class PsRiskLang(models.Model):
    id_risk = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_risk_lang'
        unique_together = (('id_risk', 'id_lang'),)


class PsScene(models.Model):
    id_scene = models.AutoField(primary_key=True)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_scene'


class PsSceneCategory(models.Model):
    id_scene = models.IntegerField()
    id_category = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_scene_category'
        unique_together = (('id_scene', 'id_category'),)


class PsSceneLang(models.Model):
    id_scene = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=100)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_scene_lang'
        unique_together = (('id_scene', 'id_lang'),)


class PsSceneProducts(models.Model):
    id_scene = models.IntegerField()
    id_product = models.IntegerField()
    x_axis = models.IntegerField()
    y_axis = models.IntegerField()
    zone_width = models.IntegerField()
    zone_height = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_scene_products'
        unique_together = (('id_scene', 'id_product', 'x_axis', 'y_axis'),)


class PsSceneShop(models.Model):
    id_scene = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_scene_shop'
        unique_together = (('id_scene', 'id_shop'),)


class PsSearchEngine(models.Model):
    id_search_engine = models.AutoField(primary_key=True)
    server = models.CharField(max_length=64)
    getvar = models.CharField(max_length=16)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_search_engine'


class PsSearchIndex(models.Model):
    id_product = models.IntegerField()
    id_word = models.IntegerField()
    weight = models.SmallIntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_search_index'
        unique_together = (('id_word', 'id_product'),)


class PsSearchWord(models.Model):
    id_word = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    word = models.CharField(max_length=15)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_search_word'
        unique_together = (('id_lang', 'id_shop', 'word'),)


class PsSekeyword(models.Model):
    id_sekeyword = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    keyword = models.CharField(max_length=256)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_sekeyword'


class PsShop(models.Model):
    id_shop = models.AutoField(primary_key=True)
    id_shop_group = models.IntegerField()
    name = models.CharField(max_length=64)
    id_category = models.IntegerField()
    id_theme = models.IntegerField()
    active = models.IntegerField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_shop'


class PsShopGroup(models.Model):
    id_shop_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    share_customer = models.IntegerField()
    share_order = models.IntegerField()
    share_stock = models.IntegerField()
    active = models.IntegerField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_shop_group'


class PsShopUrl(models.Model):
    id_shop_url = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    domain = models.CharField(max_length=150)
    domain_ssl = models.CharField(max_length=150)
    physical_uri = models.CharField(max_length=64)
    virtual_uri = models.CharField(max_length=64)
    main = models.IntegerField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_shop_url'
        unique_together = (('domain_ssl', 'physical_uri', 'virtual_uri'), ('domain', 'physical_uri', 'virtual_uri'),)


class PsSpecificPrice(models.Model):
    id_specific_price = models.AutoField(primary_key=True)
    id_specific_price_rule = models.IntegerField()
    id_cart = models.IntegerField()
    id_product = models.IntegerField()
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    id_currency = models.IntegerField()
    id_country = models.IntegerField()
    id_group = models.IntegerField()
    id_customer = models.IntegerField()
    id_product_attribute = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6)
    from_quantity = models.IntegerField()
    reduction = models.DecimalField(max_digits=20, decimal_places=6)
    reduction_type = models.CharField(max_length=10)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_specific_price'


class PsSpecificPricePriority(models.Model):
    id_specific_price_priority = models.AutoField(primary_key=True)
    id_product = models.IntegerField(unique=True)
    priority = models.CharField(max_length=80)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_specific_price_priority'
        unique_together = (('id_specific_price_priority', 'id_product'),)


class PsSpecificPriceRule(models.Model):
    id_specific_price_rule = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_shop = models.IntegerField()
    id_currency = models.IntegerField()
    id_country = models.IntegerField()
    id_group = models.IntegerField()
    from_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    reduction = models.DecimalField(max_digits=20, decimal_places=6)
    reduction_type = models.CharField(max_length=10)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_specific_price_rule'


class PsSpecificPriceRuleCondition(models.Model):
    id_specific_price_rule_condition = models.AutoField(primary_key=True)
    id_specific_price_rule_condition_group = models.IntegerField()
    type = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_specific_price_rule_condition'


class PsSpecificPriceRuleConditionGroup(models.Model):
    id_specific_price_rule_condition_group = models.AutoField(primary_key=True)
    id_specific_price_rule = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_specific_price_rule_condition_group'
        unique_together = (('id_specific_price_rule_condition_group', 'id_specific_price_rule'),)


class PsState(models.Model):
    id_state = models.AutoField(primary_key=True)
    id_country = models.IntegerField()
    id_zone = models.IntegerField()
    name = models.CharField(max_length=64)
    iso_code = models.CharField(max_length=7)
    tax_behavior = models.SmallIntegerField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_state'


class PsStatssearch(models.Model):
    id_statssearch = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    keywords = models.CharField(max_length=255)
    results = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_statssearch'


class PsStock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_warehouse = models.IntegerField()
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    reference = models.CharField(max_length=32)
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    upc = models.CharField(max_length=12, blank=True, null=True)
    physical_quantity = models.IntegerField()
    usable_quantity = models.IntegerField()
    price_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_stock'


class PsStockAvailable(models.Model):
    id_stock_available = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    id_shop = models.IntegerField()
    id_shop_group = models.IntegerField()
    quantity = models.IntegerField()
    depends_on_stock = models.IntegerField()
    out_of_stock = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_stock_available'
        unique_together = (('id_product', 'id_product_attribute', 'id_shop', 'id_shop_group'),)


class PsStockMvt(models.Model):
    id_stock_mvt = models.BigIntegerField(primary_key=True)
    id_stock = models.IntegerField()
    id_order = models.IntegerField(blank=True, null=True)
    id_supply_order = models.IntegerField(blank=True, null=True)
    id_stock_mvt_reason = models.IntegerField()
    id_employee = models.IntegerField()
    employee_lastname = models.CharField(max_length=32, blank=True, null=True)
    employee_firstname = models.CharField(max_length=32, blank=True, null=True)
    physical_quantity = models.IntegerField()
    date_add = models.DateTimeField()
    sign = models.IntegerField()
    price_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    last_wa = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    current_wa = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    referer = models.BigIntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_stock_mvt'


class PsStockMvtReason(models.Model):
    id_stock_mvt_reason = models.AutoField(primary_key=True)
    sign = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_stock_mvt_reason'


class PsStockMvtReasonLang(models.Model):
    id_stock_mvt_reason = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_stock_mvt_reason_lang'
        unique_together = (('id_stock_mvt_reason', 'id_lang'),)


class PsStore(models.Model):
    id_store = models.AutoField(primary_key=True)
    id_country = models.IntegerField()
    id_state = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64)
    postcode = models.CharField(max_length=12)
    latitude = models.DecimalField(max_digits=13, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=8, blank=True, null=True)
    hours = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    fax = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_store'


class PsStoreShop(models.Model):
    id_store = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_store_shop'
        unique_together = (('id_store', 'id_shop'),)


class PsSupplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supplier'


class PsSupplierLang(models.Model):
    id_supplier = models.IntegerField()
    id_lang = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supplier_lang'
        unique_together = (('id_supplier', 'id_lang'),)


class PsSupplierShop(models.Model):
    id_supplier = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supplier_shop'
        unique_together = (('id_supplier', 'id_shop'),)


class PsSupplyOrder(models.Model):
    id_supply_order = models.AutoField(primary_key=True)
    id_supplier = models.IntegerField()
    supplier_name = models.CharField(max_length=64)
    id_lang = models.IntegerField()
    id_warehouse = models.IntegerField()
    id_supply_order_state = models.IntegerField()
    id_currency = models.IntegerField()
    id_ref_currency = models.IntegerField()
    reference = models.CharField(max_length=64)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    date_delivery_expected = models.DateTimeField(blank=True, null=True)
    total_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    total_with_discount_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    total_tax = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    total_ti = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    discount_value_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    is_template = models.IntegerField(blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order'


class PsSupplyOrderDetail(models.Model):
    id_supply_order_detail = models.AutoField(primary_key=True)
    id_supply_order = models.IntegerField()
    id_currency = models.IntegerField()
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    reference = models.CharField(max_length=32)
    supplier_reference = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    upc = models.CharField(max_length=12, blank=True, null=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    unit_price_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    quantity_expected = models.IntegerField()
    quantity_received = models.IntegerField()
    price_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    discount_value_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    price_with_discount_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    tax_value = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    price_ti = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    tax_value_with_order_discount = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    price_with_order_discount_te = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order_detail'


class PsSupplyOrderHistory(models.Model):
    id_supply_order_history = models.AutoField(primary_key=True)
    id_supply_order = models.IntegerField()
    id_employee = models.IntegerField()
    employee_lastname = models.CharField(max_length=32, blank=True, null=True)
    employee_firstname = models.CharField(max_length=32, blank=True, null=True)
    id_state = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order_history'


class PsSupplyOrderReceiptHistory(models.Model):
    id_supply_order_receipt_history = models.AutoField(primary_key=True)
    id_supply_order_detail = models.IntegerField()
    id_employee = models.IntegerField()
    employee_lastname = models.CharField(max_length=32, blank=True, null=True)
    employee_firstname = models.CharField(max_length=32, blank=True, null=True)
    id_supply_order_state = models.IntegerField()
    quantity = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order_receipt_history'


class PsSupplyOrderState(models.Model):
    id_supply_order_state = models.AutoField(primary_key=True)
    delivery_note = models.IntegerField()
    editable = models.IntegerField()
    receipt_state = models.IntegerField()
    pending_receipt = models.IntegerField()
    enclosed = models.IntegerField()
    color = models.CharField(max_length=32, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order_state'


class PsSupplyOrderStateLang(models.Model):
    id_supply_order_state = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_supply_order_state_lang'
        unique_together = (('id_supply_order_state', 'id_lang'),)


class PsTab(models.Model):
    id_tab = models.AutoField(primary_key=True)
    id_parent = models.IntegerField()
    class_name = models.CharField(max_length=64)
    module = models.CharField(max_length=64, blank=True, null=True)
    position = models.IntegerField()
    active = models.IntegerField()
    hide_host_mode = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tab'


class PsTabAdvice(models.Model):
    id_tab = models.IntegerField()
    id_advice = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tab_advice'
        unique_together = (('id_tab', 'id_advice'),)


class PsTabLang(models.Model):
    id_tab = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tab_lang'
        unique_together = (('id_tab', 'id_lang'),)


class PsTabModulePreference(models.Model):
    id_tab_module_preference = models.AutoField(primary_key=True)
    id_employee = models.IntegerField()
    id_tab = models.IntegerField()
    module = models.CharField(max_length=255)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tab_module_preference'
        unique_together = (('id_employee', 'id_tab', 'module'),)


class PsTag(models.Model):
    id_tag = models.AutoField(primary_key=True)
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tag'


class PsTax(models.Model):
    id_tax = models.AutoField(primary_key=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3)
    active = models.IntegerField()
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tax'


class PsTaxLang(models.Model):
    id_tax = models.IntegerField()
    id_lang = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tax_lang'
        unique_together = (('id_tax', 'id_lang'),)


class PsTaxRule(models.Model):
    id_tax_rule = models.AutoField(primary_key=True)
    id_tax_rules_group = models.IntegerField()
    id_country = models.IntegerField()
    id_state = models.IntegerField()
    zipcode_from = models.CharField(max_length=12)
    zipcode_to = models.CharField(max_length=12)
    id_tax = models.IntegerField()
    behavior = models.IntegerField()
    description = models.CharField(max_length=100)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tax_rule'


class PsTaxRulesGroup(models.Model):
    id_tax_rules_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tax_rules_group'


class PsTaxRulesGroupShop(models.Model):
    id_tax_rules_group = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_tax_rules_group_shop'
        unique_together = (('id_tax_rules_group', 'id_shop'),)


class PsTheme(models.Model):
    id_theme = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    directory = models.CharField(max_length=64)
    responsive = models.IntegerField()
    default_left_column = models.IntegerField()
    default_right_column = models.IntegerField()
    product_per_page = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_theme'


class PsThemeMeta(models.Model):
    id_theme_meta = models.AutoField(primary_key=True)
    id_theme = models.IntegerField()
    id_meta = models.IntegerField()
    left_column = models.IntegerField()
    right_column = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_theme_meta'
        unique_together = (('id_theme', 'id_meta'),)


class PsThemeSpecific(models.Model):
    id_theme = models.IntegerField()
    id_shop = models.IntegerField()
    entity = models.IntegerField()
    id_object = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_theme_specific'
        unique_together = (('id_theme', 'id_shop', 'entity', 'id_object'),)


class PsThemeconfigurator(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_shop = models.IntegerField()
    id_lang = models.IntegerField()
    item_order = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    title_use = models.IntegerField()
    hook = models.CharField(max_length=100, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    target = models.IntegerField()
    image = models.CharField(max_length=100, blank=True, null=True)
    image_w = models.CharField(max_length=10, blank=True, null=True)
    image_h = models.CharField(max_length=10, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_themeconfigurator'


class PsTimezone(models.Model):
    id_timezone = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_timezone'


class PsWarehouse(models.Model):
    id_warehouse = models.AutoField(primary_key=True)
    id_currency = models.IntegerField()
    id_address = models.IntegerField()
    id_employee = models.IntegerField()
    reference = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=45)
    management_type = models.CharField(max_length=4)
    deleted = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_warehouse'


class PsWarehouseCarrier(models.Model):
    id_carrier = models.IntegerField()
    id_warehouse = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_warehouse_carrier'
        unique_together = (('id_warehouse', 'id_carrier'),)


class PsWarehouseProductLocation(models.Model):
    id_warehouse_product_location = models.AutoField(primary_key=True)
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    id_warehouse = models.IntegerField()
    location = models.CharField(max_length=64, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_warehouse_product_location'
        unique_together = (('id_product', 'id_product_attribute', 'id_warehouse'),)


class PsWarehouseShop(models.Model):
    id_shop = models.IntegerField()
    id_warehouse = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_warehouse_shop'
        unique_together = (('id_warehouse', 'id_shop'),)


class PsWebBrowser(models.Model):
    id_web_browser = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_web_browser'


class PsWebserviceAccount(models.Model):
    id_webservice_account = models.AutoField(primary_key=True)
    key = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    class_name = models.CharField(max_length=50)
    is_module = models.IntegerField()
    module_name = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_webservice_account'


class PsWebserviceAccountShop(models.Model):
    id_webservice_account = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_webservice_account_shop'
        unique_together = (('id_webservice_account', 'id_shop'),)


class PsWebservicePermission(models.Model):
    id_webservice_permission = models.AutoField(primary_key=True)
    resource = models.CharField(max_length=50)
    method = models.CharField(max_length=6)
    id_webservice_account = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_webservice_permission'
        unique_together = (('resource', 'method', 'id_webservice_account'),)


class PsWishlist(models.Model):
    id_wishlist = models.AutoField(primary_key=True)
    id_customer = models.IntegerField()
    token = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    counter = models.IntegerField(blank=True, null=True)
    id_shop = models.IntegerField(blank=True, null=True)
    id_shop_group = models.IntegerField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_wishlist'


class PsWishlistEmail(models.Model):
    id_wishlist = models.IntegerField()
    email = models.CharField(max_length=128)
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_wishlist_email'


class PsWishlistProduct(models.Model):
    id_wishlist_product = models.AutoField(primary_key=True)
    id_wishlist = models.IntegerField()
    id_product = models.IntegerField()
    id_product_attribute = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_wishlist_product'


class PsWishlistProductCart(models.Model):
    id_wishlist_product = models.IntegerField()
    id_cart = models.IntegerField()
    quantity = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_wishlist_product_cart'


class PsZone(models.Model):
    id_zone = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    active = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_zone'


class PsZoneShop(models.Model):
    id_zone = models.IntegerField()
    id_shop = models.IntegerField()

    class Meta(MetaCore):
        managed = False
        db_table = 'ps_zone_shop'
        unique_together = (('id_zone', 'id_shop'),)
