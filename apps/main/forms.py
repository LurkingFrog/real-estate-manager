from django import forms

from apps.main.models import Address, Agent


class ManageAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        exclude = ['closed_properties', 'business_address']

    def __init__(self, *args, **kwargs):
        super(ManageAgentForm, self).__init__(*args, **kwargs)
        if self.instance:
            kwargs['instance'] = self.instance.business_address
            
        self.address_form = ManageAddressForm(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if self.address_form.is_valid():
            return super(ManageAgentForm, self).clean(*args, **kwargs)
        else:
            raise forms.ValidationError("Address Issues")

    def save(self, *args, **kwargs):
        address = self.address_form.save()
        agent = super(ManageAgentForm, self).save(*args, **kwargs)
        agent.business_address = address
        agent.save()

        return agent


class ManageAddressForm(forms.ModelForm):
    class Meta:
        model = Address

    def clean(self, *args, **kwargs):
        # TODO: Add ignore if no address info filled in
        data = super(ManageAddressForm, self).clean(*args, **kwargs)

        return data
