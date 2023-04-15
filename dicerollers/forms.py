from django import forms

OPTION_CHOICES=[
    ('no', 'No, just roll please.'),
    ('gwf', 'Great Weapon Fighter'),
    ('ea', 'Elemental Adept'),
]

class DiceRollForm(forms.Form):
    dice = forms.IntegerField(min_value=1, max_value=100, label='Number of dice to roll')
    sides = forms.IntegerField(min_value=1, max_value=100, label='Number of sides on each die')
    option = forms.CharField(label='Any additional effects on this role?', widget=forms.Select(choices=OPTION_CHOICES))