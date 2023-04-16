from django import forms

OPTION_CHOICES=[
    ('no', 'No, just roll please.'),
    ('gwf', 'Great Weapon Fighter'),
    ('ea', 'Elemental Adept'),
]

CRIT_TYPE=[
    ('a', 'Each die gets rolled an additional time'),
    ('b', 'The total damage is multiplied by two'),
    ('c', 'All dice roll maximum'),
    ('d', 'All dice roll maximum, then get rolled again'),

]

class DiceRollForm(forms.Form):
    dice = forms.IntegerField(min_value=1, max_value=100, label='Number of dice to roll')
    sides = forms.IntegerField(min_value=1, max_value=100, label='Number of sides on each die')
    modifier = forms.IntegerField(min_value=-100, max_value=100, label='Modifier to roll')
    option = forms.CharField(label='Any additional effects on this roll?', widget=forms.Select(choices=OPTION_CHOICES))
    crit = forms.BooleanField(label='Is this a critical hit?', required=False)
    crit_type = forms.CharField(label='What critical damage formula do you use?', widget=forms.Select(choices=CRIT_TYPE))