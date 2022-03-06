# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Index, Integer, Numeric, SmallInteger, String, Text, text
from sqlalchemy.dialects.mysql.types import BIT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ActType(Base):
    __tablename__ = 'ActType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class AiCommandType(Base):
    __tablename__ = 'AiCommandType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class AiType(Base):
    __tablename__ = 'AiType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class BOOL(Base):
    __tablename__ = 'BOOL'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class EnemyState(Base):
    __tablename__ = 'EnemyState'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Equip(Base):
    __tablename__ = 'Equip'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    ling_info = Column(Text)
    ling_name = Column(Text)
    icon = Column(Text)
    model = Column(Text)
    texture = Column(Text)
    lhand = Column(Text)
    rhand = Column(Text)
    tianhe_lv_lmt = Column(Integer)
    lingsha_lv_lmt = Column(Integer)
    mengli_lv_lmt = Column(Integer)
    ziying_lv_lmt = Column(Integer)
    attached_effect = Column(Text)
    price = Column(Integer)
    ling_capacity = Column(Integer)
    skill_id = Column(Integer)
    forge_potential = Column(Integer)
    max_hp = Column(Integer)
    additional_rage = Column(Integer)
    max_mp = Column(Integer)
    physical = Column(Integer)
    toughness = Column(Integer)
    speed = Column(Integer)
    lucky = Column(Integer)
    will = Column(Integer)
    water = Column(Integer)
    fire = Column(Integer)
    thunder = Column(Integer)
    air = Column(Integer)
    earth = Column(Integer)
    physical_additional = Column(Integer)
    water_additional = Column(Integer)
    fire_additional = Column(Integer)
    thunder_additional = Column(Integer)
    air_additional = Column(Integer)
    earth_additional = Column(Integer)
    physical_extract = Column(Float)
    water_extract = Column(Float)
    fire_extract = Column(Float)
    thunder_extract = Column(Float)
    air_extract = Column(Float)
    earth_extract = Column(Float)
    physical_react = Column(Float)
    water_react = Column(Float)
    fire_react = Column(Float)
    thunder_react = Column(Float)
    air_react = Column(Float)
    earth_react = Column(Float)
    additional_critical = Column(Float)
    fend_off = Column(Float)
    additional_hitting = Column(Float)
    pay_for_spare = Column(Float)
    ef1 = Column(Text)
    ef2 = Column(Text)
    ef3 = Column(Text)


class EquipClas(Base):
    __tablename__ = 'EquipClass'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class EquipRelation(Base):
    __tablename__ = 'EquipRelation'

    id = Column(Integer, primary_key=True)
    _class = Column('class', Integer)
    type = Column(Integer)


class EquipType(Base):
    __tablename__ = 'EquipType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class GameQuestion(Base):
    __tablename__ = 'GameQuestion'

    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer1 = Column(Text)
    answer2 = Column(Text)
    answer3 = Column(Text)
    right_answer = Column(Integer)
    db = Column(Integer)


class Good(Base):
    __tablename__ = 'Good'

    id = Column(Integer, primary_key=True)
    shop_id = Column(Text)
    goods_id = Column(Integer)
    goods_type = Column(Integer)
    open_condition = Column(Integer)
    open_num = Column(Integer)


class GoodsType(Base):
    __tablename__ = 'GoodsType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Magic(Base):
    __tablename__ = 'Magic'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    attribute = Column(Text)
    ai_cmd_type = Column(Integer)
    target = Column(Integer)
    wuling = Column(Integer)
    need_total_used_point = Column(Integer)
    need_point = Column(Integer)
    parent_magic = Column(Integer)
    attached_skill = Column(Integer)
    consumed_mp = Column(Integer)
    act_type = Column(Integer)
    hit_extra = Column(Float)
    animation = Column(Text)
    effect = Column(Text)
    target_ef = Column(Text)
    target_bind = Column(Text)


class MapInfo(Base):
    __tablename__ = 'MapInfo'

    id = Column(Integer, primary_key=True)
    string_id = Column(Integer)


class Mission(Base):
    __tablename__ = 'Mission'

    depended_id = Column(Integer, primary_key=True)
    trunk = Column(Integer)
    quest_id = Column(Integer)
    name = Column(Text)
    picture = Column(Text)
    description = Column(Text)
    story_per = Column(Float)
    story_show = Column(Integer)


class Monster(Base):
    __tablename__ = 'Monster'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    icon = Column(Text)
    model = Column(Text)
    texture = Column(Text)
    description = Column(Text)
    race = Column(Integer)
    is_boss = Column(Integer)
    ai_type = Column(Integer)
    max_hp = Column(Integer)
    additional_rage = Column(Integer)
    max_mp = Column(Integer)
    physical = Column(Integer)
    toughness = Column(Integer)
    speed = Column(Integer)
    lucky = Column(Integer)
    will = Column(Integer)
    water = Column(Integer)
    fire = Column(Integer)
    thunder = Column(Integer)
    air = Column(Integer)
    earth = Column(Integer)
    physical_additional = Column(Integer)
    water_additional = Column(Integer)
    fire_additional = Column(Integer)
    thunder_additional = Column(Integer)
    air_additional = Column(Integer)
    earth_additional = Column(Integer)
    physical_extract = Column(Float)
    water_extract = Column(Float)
    fire_extract = Column(Float)
    thunder_extract = Column(Float)
    air_extract = Column(Float)
    earth_extract = Column(Float)
    physical_react = Column(Float)
    water_react = Column(Float)
    fire_react = Column(Float)
    thunder_react = Column(Float)
    air_react = Column(Float)
    earth_react = Column(Float)
    additional_critical = Column(Float)
    fend_off = Column(Float)
    additional_hitting = Column(Float)
    counterpunch_rate = Column(Float)
    pay_for_spare = Column(Float)
    experience = Column(Integer)
    level = Column(Integer)
    physical_atk_target = Column(Integer)
    physical_atk_range = Column(Integer)
    skill1 = Column(Integer)
    skill2 = Column(Integer)
    skill3 = Column(Integer)
    skill4 = Column(Integer)
    skill5 = Column(Integer)
    skill6 = Column(Integer)
    stolen_property = Column(Integer)
    stolen_number = Column(Integer)
    stolen_money = Column(Integer)
    drop1id = Column(Integer)
    drop1rate = Column(Float)
    drop2id = Column(Integer)
    drop2rate = Column(Float)
    drop3id = Column(Integer)
    drop3rate = Column(Float)
    drop4id = Column(Integer)
    drop4rate = Column(Float)
    max_drop_money = Column(Integer)
    min_drop_money = Column(Integer)
    atk_added_rage = Column(Integer)
    rage = Column(Integer)
    sound_wounded1 = Column(Text)
    sound_wounded2 = Column(Text)
    sound_wounded3 = Column(Text)
    sound_wounded4 = Column(Text)
    sound_wounded5 = Column(Text)
    final_hit = Column(Text)
    act_type = Column(Integer)
    count = Column(Integer)
    bondage_immunity = Column(Float)
    seal_immunity = Column(Float)
    forbiden_immunity = Column(Float)
    sleep_immunity = Column(Float)
    mad_immunity = Column(Float)
    disorder_immunity = Column(Float)
    water_immunity = Column(Float)
    fire_immunity = Column(Float)
    thunder_immunity = Column(Float)
    air_immunity = Column(Float)
    earth_immunity = Column(Float)
    siphon_immunity = Column(Float)
    mortal_immunity = Column(Float)


class PhysicalAttackTarget(Base):
    __tablename__ = 'PhysicalAttackTarget'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class PhysicalAttackType(Base):
    __tablename__ = 'PhysicalAttackType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Prescription(Base):
    __tablename__ = 'Prescription'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    attribute = Column(Text)
    type = Column(Integer)
    sword = Column(Integer)
    dsword = Column(Integer)
    instrument = Column(Integer)
    helm = Column(Integer)
    armor = Column(Integer)
    boot = Column(Integer)
    ornament = Column(Integer)
    product_id = Column(Integer)
    need_potential = Column(Integer)
    need_ling = Column(Integer)
    skill_id = Column(Integer)
    price = Column(Integer)
    material1 = Column(Integer)
    material1num = Column(Integer)
    material2 = Column(Integer)
    material2num = Column(Integer)
    material3 = Column(Integer)
    material3num = Column(Integer)
    material4 = Column(Integer)
    material4num = Column(Integer)
    max_hp = Column(Integer)
    added_rage = Column(Integer)
    max_mp = Column(Integer)
    physical = Column(Integer)
    defence = Column(Integer)
    speed = Column(Integer)
    lucky = Column(Integer)
    will = Column(Integer)
    water = Column(Integer)
    fire = Column(Integer)
    thunder = Column(Integer)
    air = Column(Integer)
    earth = Column(Integer)
    physical_add = Column(Integer)
    water_add = Column(Integer)
    fire_add = Column(Integer)
    thunder_add = Column(Integer)
    air_add = Column(Integer)
    earth_add = Column(Integer)
    physical_extract = Column(Float)
    water_extract = Column(Float)
    fire_extract = Column(Float)
    thunder_extract = Column(Float)
    air_extract = Column(Float)
    earth_extract = Column(Float)
    physical_react = Column(Float)
    water_react = Column(Float)
    fire_react = Column(Float)
    thunder_react = Column(Float)
    air_react = Column(Float)
    earth_react = Column(Float)
    added_critical = Column(Float)
    fend_off = Column(Float)
    added_hitting = Column(Float)
    pay_for_spare = Column(Float)
    calc_type = Column(Integer)
    ef2 = Column(Text)
    ef3 = Column(Text)
    ef4 = Column(Text)


class PrescriptionType(Base):
    __tablename__ = 'PrescriptionType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Property(Base):
    __tablename__ = 'Property'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    attribute = Column(Text)
    icon = Column(Text)
    model = Column(Text)
    texture = Column(Text)
    attached_effect = Column(Text)
    type = Column(Integer)
    property_level = Column(Integer)
    target = Column(Integer)
    tianhe_can_use = Column(Integer)
    lingsha_can_use = Column(Integer)
    mengli_can_use = Column(Integer)
    ziying_can_use = Column(Integer)
    ai_cmd_type = Column(Integer)
    price = Column(Integer)
    attached_skill = Column(Integer)
    candrop = Column(Integer)
    canuse_in_sys_ui = Column(Integer)
    atk_type = Column(Integer)
    atk_delay = Column(Float)


class PropertyClas(Base):
    __tablename__ = 'PropertyClass'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class PropertyLevel(Base):
    __tablename__ = 'PropertyLevel'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Race(Base):
    __tablename__ = 'Race'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    icon = Column(Text)
    model = Column(Text)
    texture = Column(Text)
    race = Column(Integer)
    tianhe_favor = Column(Integer)
    lingsha_favor = Column(Integer)
    mengli_favor = Column(Integer)
    ziying_favor = Column(Integer)
    max_hp = Column(Integer)
    additional_rage = Column(Integer)
    max_mp = Column(Integer)
    physical = Column(Integer)
    toughness = Column(Integer)
    speed = Column(Integer)
    lucky = Column(Integer)
    will = Column(Integer)
    water = Column(Integer)
    fire = Column(Integer)
    thunder = Column(Integer)
    air = Column(Integer)
    earth = Column(Integer)
    physical_additional = Column(Integer)
    water_additional = Column(Integer)
    fire_additional = Column(Integer)
    thunder_additional = Column(Integer)
    air_additional = Column(Integer)
    earth_additional = Column(Integer)
    physical_extract = Column(Float)
    water_extract = Column(Float)
    fire_extract = Column(Float)
    thunder_extract = Column(Float)
    air_extract = Column(Float)
    earth_extract = Column(Float)
    physical_react = Column(Float)
    water_react = Column(Float)
    fire_react = Column(Float)
    thunder_react = Column(Float)
    air_react = Column(Float)
    earth_react = Column(Float)
    additional_critical = Column(Float)
    fend_off = Column(Float)
    additional_hitting = Column(Float)
    pay_for_spare = Column(Float)
    physical_atk_target = Column(Integer)
    physical_atk_range = Column(Integer)
    sound_wounded1 = Column(Text)
    sound_wounded2 = Column(Text)
    sound_wounded3 = Column(Text)


class SPComboMartial(Base):
    __tablename__ = 'SPComboMartial'

    id = Column(Integer, primary_key=True)
    f1id = Column(Integer, nullable=False)
    f1lvl = Column(Integer, nullable=False)
    f2id = Column(Integer, nullable=False)
    f2lvl = Column(Integer, nullable=False)
    user_flag = Column(BIT(8), nullable=False)


class SPEnemyLevel(Base):
    __tablename__ = 'SPEnemyLevel'

    k1id = Column(Integer, primary_key=True)
    p01 = Column(Integer)
    p02 = Column(Integer)
    p03 = Column(Integer)
    p04 = Column(Integer)
    p05 = Column(Integer)
    p06 = Column(Integer)
    p07 = Column(Integer)
    p08 = Column(Integer)
    p09 = Column(Integer)
    p10 = Column(Integer)
    p11 = Column(Integer)
    p12 = Column(Integer)
    p13 = Column(Integer)
    p14 = Column(Integer)
    p15 = Column(Integer)
    p16 = Column(Integer)
    p17 = Column(Integer)
    p18 = Column(Integer)
    p19 = Column(Integer)
    p20 = Column(Integer)
    p21 = Column(Integer)
    p22 = Column(Integer)
    p23 = Column(Integer)
    p24 = Column(Integer)


class SPFighterHelp(Base):
    __tablename__ = 'SPFighterHelp'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class SPFighterTable1(Base):
    __tablename__ = 'SPFighterTable1'

    rec_id = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    name = Column(String(16), nullable=False)
    lvl = Column(Integer, nullable=False)
    need = Column(Integer, nullable=False, server_default=text("'-1'"))
    func = Column(Integer, nullable=False, server_default=text("'0'"))
    param1 = Column(Integer, nullable=False, server_default=text("'0'"))
    param2 = Column(Integer, nullable=False, server_default=text("'0'"))
    param3 = Column(Integer, nullable=False, server_default=text("'0'"))
    param4 = Column(Integer, nullable=False, server_default=text("'0'"))


class SPFighterTable2(Base):
    __tablename__ = 'SPFighterTable2'

    rec_id = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    name = Column(String(16), nullable=False)
    lvl = Column(Integer, nullable=False)
    need = Column(Integer, nullable=False, server_default=text("'-1'"))
    p02 = Column(Integer, nullable=False, server_default=text("'0'"))
    p03 = Column(Integer, nullable=False, server_default=text("'0'"))
    p04 = Column(Integer, nullable=False, server_default=text("'0'"))
    addition_rate = Column(Integer, nullable=False, server_default=text("'0'"))
    base_effect = Column(Integer, nullable=False, server_default=text("'0'"))
    p07 = Column(Integer, nullable=False, server_default=text("'0'"))
    p08 = Column(Integer, nullable=False, server_default=text("'0'"))
    p09 = Column(Integer, nullable=False, server_default=text("'0'"))
    work_range = Column(Integer, nullable=False, server_default=text("'0'"))
    times = Column(Integer, nullable=False, server_default=text("'0'"))
    mp_consume = Column(Integer, nullable=False, server_default=text("'0'"))
    p13 = Column(Integer, nullable=False, server_default=text("'0'"))
    anim_id = Column(Integer, nullable=False, server_default=text("'0'"))
    p15 = Column(Integer, nullable=False, server_default=text("'0'"))
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    p17 = Column(Integer, nullable=False, server_default=text("'0'"))
    p18 = Column(Integer, nullable=False, server_default=text("'0'"))
    p19 = Column(Integer, nullable=False, server_default=text("'0'"))
    p21 = Column(Integer, nullable=False, server_default=text("'0'"))


class SPItemDatum(Base):
    __tablename__ = 'SPItemData'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    strength = Column(Integer, nullable=False, server_default=text("'0'"))
    accuracy = Column(Integer, nullable=False, server_default=text("'0'"))
    crit_rate = Column(Integer, nullable=False, server_default=text("'0'"))
    defence = Column(Integer, nullable=False, server_default=text("'0'"))
    agility = Column(Integer, nullable=False, server_default=text("'0'"))
    quick = Column(Integer, nullable=False, server_default=text("'0'"))
    intelligence = Column(Integer, nullable=False, server_default=text("'0'"))
    mp = Column(Integer, nullable=False, server_default=text("'0'"))
    require_level = Column(Integer, nullable=False, server_default=text("'0'"))
    price = Column(Integer, nullable=False, server_default=text("'0'"))
    user_flag = Column(BIT(16), nullable=False)
    func = Column(Integer, nullable=False, server_default=text("'0'"))
    func_param = Column(Integer, nullable=False, server_default=text("'0'"))
    whence = Column(Integer, nullable=False, server_default=text("'0'"))
    sub_func1 = Column(Integer, nullable=False, server_default=text("'0'"))
    sub_func2 = Column(Integer, nullable=False, server_default=text("'0'"))
    act_range = Column(Integer, nullable=False, server_default=text("'0'"))
    unknown7 = Column(Integer, nullable=False, server_default=text("'0'"))


class SPItemHelp(Base):
    __tablename__ = 'SPItemHelp'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class SPKindle1(Base):
    __tablename__ = 'SPKindle1'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    model = Column(Integer, nullable=False)
    race = Column(Integer, nullable=False)


class SPKindle2(Base):
    __tablename__ = 'SPKindle2'

    id = Column(Integer, primary_key=True)
    k1id = Column(Integer, nullable=False)
    p_p1 = Column(Integer, nullable=False)
    p_p2 = Column(Integer, nullable=False)
    p_p3 = Column(Integer, nullable=False)
    p_p4 = Column(Integer, nullable=False)
    p_p5 = Column(Integer, nullable=False)
    name = Column(String(16), nullable=False)
    s_p02 = Column(Integer, nullable=False)
    s_p03 = Column(Integer, nullable=False)
    s_p04 = Column(Integer, nullable=False)
    s_p05 = Column(Integer, nullable=False)
    s_p06 = Column(Integer, nullable=False)
    s_p07 = Column(Integer, nullable=False)
    s_p08 = Column(Integer, nullable=False)
    s_p09 = Column(Integer, nullable=False)
    s_p10 = Column(Integer, nullable=False)
    s_p12 = Column(Integer, nullable=False)
    s_p13 = Column(Integer, nullable=False)


class SPKindle3(Base):
    __tablename__ = 'SPKindle3'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    k1id = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    p04 = Column(Integer, nullable=False)
    steal1 = Column(Integer, nullable=False)
    steal1num = Column(Integer, nullable=False)
    steal1chance = Column(Integer, nullable=False)
    steal2 = Column(Integer, nullable=False)
    steal2num = Column(Integer, nullable=False)
    steal2chance = Column(Integer, nullable=False)
    drop_item = Column(Integer, nullable=False)
    drop_chance = Column(Integer, nullable=False)
    p13 = Column(Integer, nullable=False)
    p14 = Column(Integer, nullable=False)
    p15 = Column(Integer, nullable=False)
    fight_type = Column(Integer, nullable=False)
    f1 = Column(Integer, nullable=False)
    f1lvl = Column(Integer, nullable=False)
    f2 = Column(Integer, nullable=False)
    f2lvl = Column(Integer, nullable=False)
    f3 = Column(Integer, nullable=False)
    f3lvl = Column(Integer, nullable=False)
    f4 = Column(Integer, nullable=False)
    f4lvl = Column(Integer, nullable=False)


class SPMission(Base):
    __tablename__ = 'SPMission'

    rec_id = Column(Integer, primary_key=True)
    f1 = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False)
    content = Column(String(512), nullable=False, server_default=text("''"))
    f2 = Column(Integer, nullable=False)
    f3 = Column(Integer, nullable=False)


class SPRange(Base):
    __tablename__ = 'SPRange'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class SPRoleManDefault(Base):
    __tablename__ = 'SPRoleManDefault'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    unknown = Column(Integer, nullable=False, server_default=text("'0'"))
    model = Column(Integer, nullable=False, server_default=text("'0'"))
    prop03 = Column(Integer, nullable=False, server_default=text("'0'"))
    own_item1 = Column(Integer, nullable=False, server_default=text("'0'"))
    own_count1 = Column(Integer, nullable=False, server_default=text("'0'"))
    own_item2 = Column(Integer, nullable=False, server_default=text("'0'"))
    own_count2 = Column(Integer, nullable=False, server_default=text("'0'"))
    prop20 = Column(Integer, nullable=False, server_default=text("'0'"))
    prop21 = Column(Integer, nullable=False, server_default=text("'0'"))
    f1 = Column(Integer, nullable=False, server_default=text("'0'"))
    f1lvl = Column(Integer, nullable=False, server_default=text("'0'"))
    f2 = Column(Integer, nullable=False, server_default=text("'0'"))
    f2lvl = Column(Integer, nullable=False, server_default=text("'0'"))
    f3 = Column(Integer, nullable=False, server_default=text("'0'"))
    f3lvl = Column(Integer, nullable=False, server_default=text("'0'"))


class Scene(Base):
    __tablename__ = 'Scene'

    id = Column(Integer, primary_key=True)
    scene = Column(Text)
    section = Column(Text)
    name = Column(Text)
    type = Column(Integer)
    earthball = Column(Integer)


class SceneItem(Base):
    __tablename__ = 'SceneItem'

    id = Column(Integer, primary_key=True)
    scene = Column(String(512), nullable=False)
    section = Column(String(512), nullable=False)
    item_id = Column(String(512), nullable=False)
    model_path = Column(String(512), nullable=False)
    model = Column(String(512), nullable=False)
    texture = Column(String(512), nullable=False)
    coor_x = Column(Float, nullable=False)
    coor_y = Column(Float, nullable=False)
    coor_z = Column(Float, nullable=False)
    equip_id = Column(Integer, server_default=text("'0'"))
    property_id = Column(Integer, server_default=text("'0'"))
    item_num = Column(Integer, server_default=text("'0'"))
    money = Column(Integer, server_default=text("'0'"))
    item1id = Column(Integer, server_default=text("'0'"))
    item1num = Column(Integer, server_default=text("'0'"))
    item2id = Column(Integer, server_default=text("'0'"))
    item2num = Column(Integer, server_default=text("'0'"))
    item3id = Column(Integer, server_default=text("'0'"))
    item3num = Column(Integer, server_default=text("'0'"))
    item4id = Column(Integer, server_default=text("'0'"))
    item4num = Column(Integer, server_default=text("'0'"))
    item5id = Column(Integer, server_default=text("'0'"))
    item5num = Column(Integer, server_default=text("'0'"))
    item6id = Column(Integer, server_default=text("'0'"))
    item6num = Column(Integer, server_default=text("'0'"))
    item_money = Column(Integer, server_default=text("'0'"))


class SceneName(Base):
    __tablename__ = 'SceneName'

    id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)


class ShopProperty(Base):
    __tablename__ = 'ShopProperty'

    id = Column(String(100), primary_key=True)
    name = Column(Text)
    position = Column(Text)
    type = Column(Integer)


class ShopType(Base):
    __tablename__ = 'ShopType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Skill(Base):
    __tablename__ = 'Skill'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    triger = Column(Integer)
    exist_time = Column(Integer)
    function = Column(Integer)
    param1 = Column(Float)
    param2 = Column(Float)
    param3 = Column(Float)
    param4 = Column(Float)
    param5 = Column(Float)
    param6 = Column(Float)
    param7 = Column(Float)
    param8 = Column(Float)
    param9 = Column(Float)
    attached_skill = Column(Integer)
    mutex_id = Column(Integer)
    status_id = Column(Integer)
    ef = Column(Text)
    bind = Column(Text)
    ef1 = Column(Text)
    bind1 = Column(Text)


class SkillTarget(Base):
    __tablename__ = 'SkillTarget'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class SkillTrigerType(Base):
    __tablename__ = 'SkillTrigerType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class SkillType(Base):
    __tablename__ = 'SkillType'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Stunt(Base):
    __tablename__ = 'Stunt'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    attribute = Column(Text)
    ai_cmd_type = Column(Integer)
    target = Column(Integer)
    tianhe_lv_lmt = Column(Integer)
    lingsha_lv_lmt = Column(Integer)
    mengli_lv_lmt = Column(Integer)
    ziying_lv_lmt = Column(Integer)
    attached_skill = Column(Integer)
    consumed_rage = Column(Integer)
    consume1 = Column(Integer)
    consume1num = Column(Integer)
    consume2 = Column(Integer)
    consume2num = Column(Integer)
    consume3 = Column(Integer)
    consume3num = Column(Integer)
    consume4 = Column(Integer)
    consume4num = Column(Integer)
    consume5 = Column(Integer)
    consume5num = Column(Integer)
    consumed_money = Column(Integer)
    property_id = Column(Integer)
    skill_depended = Column(Integer)
    act_type = Column(Integer)
    hit_extra = Column(Float)
    animation = Column(Text)
    effect = Column(Text)
    target_ef = Column(Text)
    target_bind = Column(Text)
    model = Column(Text)


class TeamState(Base):
    __tablename__ = 'TeamState'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class UpgradeDatum(Base):
    __tablename__ = 'UpgradeData'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer)
    level = Column(Integer)
    experience = Column(Integer)
    max_hp = Column(Integer)
    additional_rage = Column(Integer)
    max_mp = Column(Integer)
    physical = Column(Integer)
    toughness = Column(Integer)
    speed = Column(Integer)
    lucky = Column(Integer)
    will = Column(Integer)
    water = Column(Integer)
    fire = Column(Integer)
    thunder = Column(Integer)
    air = Column(Integer)
    earth = Column(Integer)
    physical_additional = Column(Integer)
    water_additional = Column(Integer)
    fire_additional = Column(Integer)
    thunder_additional = Column(Integer)
    air_additional = Column(Integer)
    earth_additional = Column(Integer)
    physical_extract = Column(Float)
    water_extract = Column(Float)
    fire_extract = Column(Float)
    thunder_extract = Column(Float)
    air_extract = Column(Float)
    earth_extract = Column(Float)
    physical_react = Column(Float)
    water_react = Column(Float)
    fire_react = Column(Float)
    thunder_react = Column(Float)
    air_react = Column(Float)
    earth_react = Column(Float)
    additional_critical = Column(Float)
    fend_off = Column(Float)
    additional_hitting = Column(Float)
    pay_for_spare = Column(Float)


class WuLing(Base):
    __tablename__ = 'WuLing'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=False)


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    checkin = Column(DateTime, nullable=False, unique=True)
    checkout = Column(DateTime, nullable=False, unique=True)
    comments = Column(String(256), server_default=text("''"))


class Stock(Base):
    __tablename__ = 'stock'
    __table_args__ = (
        Index('uniq_trade', 'date', 'code', 'operation', 'price', unique=True),
    )

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    code = Column(String(6), nullable=False)
    name = Column(String(16), nullable=False)
    operation = Column(String(10), nullable=False)
    volume = Column(SmallInteger, nullable=False)
    balance = Column(Integer, nullable=False, server_default=text("'0'"))
    price = Column(Numeric(6, 3), nullable=False)
    turnover = Column(Numeric(8, 3), nullable=False)
    amount = Column(Numeric(8, 3), nullable=False)
    brokerage = Column(Numeric(5, 3), nullable=False)
    stamps = Column(Numeric(5, 3), nullable=False)
    transfer_fee = Column(Numeric(4, 3), nullable=False, server_default=text("'0.000'"))
