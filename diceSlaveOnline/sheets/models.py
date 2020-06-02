from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SheetGroup(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def SheetGroupName(self):
        return str(self.name)

class Sheet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    hidden = models.BooleanField(default=False)

    name = models.CharField(max_length=100)

    sheetGroup = models.ForeignKey("SheetGroup", on_delete=models.CASCADE, default=1)

    Class = models.CharField(max_length=100, default="")
    background = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    xp = models.IntegerField()
    level = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    strengthMod = models.IntegerField()
    dexterityMod = models.IntegerField()
    constitutionMod = models.IntegerField()
    intelligenceMod = models.IntegerField()
    wisdomMod = models.IntegerField()
    charismaMod = models.IntegerField()

    proficiency = models.IntegerField(default=2)

    acrobatics = models.BooleanField(default=False)
    animalHandling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleightOfHand = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)

    sStrength = models.BooleanField(verbose_name="Saving Throw: Strength")
    sDexterity = models.BooleanField(verbose_name="Saving Throw: Dexterity")
    sConstitution = models.BooleanField(verbose_name="Saving Throw: Constitution")
    sIntelligence = models.BooleanField(verbose_name="Saving Throw: Intelligence")
    sWisdom = models.BooleanField(verbose_name="Saving Throw: Wisdom")
    sCharisma = models.BooleanField(verbose_name="Saving Throw: Charisma")

    otherProficiencies = models.CharField(max_length=250)
    languages = models.CharField(max_length=250)
    copper = models.IntegerField()
    silver = models.IntegerField()
    gold = models.IntegerField()
    platinum = models.IntegerField()

    armorClass = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()
    maxHitPoints = models.IntegerField()
    hitPoints = models.IntegerField()
    hitDice = models.CharField(max_length=250)
    sDeathSave1 = models.BooleanField(default=False)
    sDeathSave2 = models.BooleanField(default=False)
    sDeathSave3 = models.BooleanField(default=False)
    fDeathSave1 = models.BooleanField(default=False)
    fDeathSave2 = models.BooleanField(default=False)
    fDeathSave3 = models.BooleanField(default=False)

    personalityTraits = models.CharField(max_length=250)
    ideals = models.CharField(max_length=250)
    bonds = models.CharField(max_length=250)
    flaws = models.CharField(max_length=250)
    featuresTraits = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def sheetGroupValue(self):
        return str(self.sheetGroup)

class Spell(models.Model):
    sht = models.ForeignKey(Sheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    name = models.CharField(max_length=50)
    reference = models.URLField(max_length=200, verbose_name="Link for Reference")

    level_choices = (
        ('cantrip', 'Cantrip'),
        ('infusion', 'Infusion'),
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th')
    )
    level = models.CharField(max_length=100, choices=level_choices, default='cantrip')
    
    type_choices = (
        ('offensive', 'Offensive'),
        ('normal', 'Normal'),
    )
    Type = models.CharField(max_length=100, choices=type_choices, default='normal')


class Item(models.Model):
    sht = models.ForeignKey(Sheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)
    reference = models.URLField(max_length=200, verbose_name="Link for Reference", blank=True, null=True, default="https://roll20.net/compendium/dnd5e/Items%20List#content")

    type_choices = (
        ('weapon', 'Weapon'),
        ('item', 'Item'),
    )
    Type = models.CharField(max_length=100, choices=type_choices, default='item')
    equipped = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Skill(models.Model):
    sht = models.ForeignKey(Sheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    nameChoices = [
        ('acrobatics', 'Acrobatics'),
        ('animalHandling', 'Animal Handling'),
        ('arcana', 'Arcana'),
        ('athletics', 'Athletics'),
        ('deception', 'Deception'),
        ('history', 'History'),
        ('insight', 'Insight'),
        ('intimidation', 'Intimidation'),
        ('investigation', 'Investigation'),
        ('medicine', 'Medicine'),
        ('nature', 'Nature'),
        ('perception', 'Perception'),
        ('performance', 'Performance'),
        ('persuasion', 'Persuasion'),
        ('religion', 'Religion'),
        ('sleightOfHand', 'Sleight of Hand'),
        ('stealth', 'Stealth'),
        ('survival', 'Survival'),
    ]

    name = models.CharField(max_length=100, choices=nameChoices, default="")
    mod = models.IntegerField()

    def __str__(self):
        return self.name