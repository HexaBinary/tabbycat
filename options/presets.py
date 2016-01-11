
class PreferencesPreset:
    def __init__(self):
        self.show_in_list                             = False

class AustralsPreferences(PreferencesPreset):
    """ 3v3 with replies, chosen motions, intermediary bubbles and 1up/1down. Compliant to AIDA rules """
    def __init__(self):
        self.name                                     = "Australs"
        self.show_in_list                             = True
        # Scoring
        self.scoring__score_min                        = 68.0
        self.scoring__score_max                        = 82.0
        self.scoring__score_step                       = 1.0
        self.scoring__reply_score_min                  = 34.0
        self.scoring__reply_score_max                  = 41.0
        self.scoring__reply_score_step                 = 0.5
        self.scoring__maximum_margin                   = 15.0 # TODO= check this
        # Draws
        self.draw_rules__avoid_same_institution        = True
        self.draw_rules__avoid_team_history            = True
        self.draw_rules__draw_odd_bracket              = 'intermediate_bubble_up_down'
        self.draw_rules__draw_side_allocations         = 'balance'
        self.draw_rules__draw_pairing_method           = 'slide'
        self.draw_rules__draw_avoid_conflicts          = 'one_up_one_down'
        # Debate Rules
        self.debate_rules__substantive_speakers        = 3
        self.debate_rules__reply_scores_enabled        = True
        self.debate_rules__motion_vetoes_enabled       = True
        # Standings Rules
        self.standings__standings_missed_debates       = 2 # TODO= check this
        self.standings__team_standings_rule            = 'australs'
        self.standings__speaker_standings_rule         = 'australs'


class AustralianEastersPreferences(AustralsPreferences):
    """ 3v3 without replies, with set motions, novices, intermediary bubbles and 1up/1down. Compliant to AIDA rules """
    def __init__(self):
        self.name                                      = "Australian Easters"
        self.show_in_list                              = True
        # Scoring= easters has a lower range
        self.scoring__score_min                        = 70.0
        self.scoring__score_max                        = 80.0
        # TODO= pretty sure this is constitutional
        self.scoring__maximum_margin                   = 15.0
        # Debate Rules= no replies; singular motions
        self.debate_rules__reply_scores_enabled        = False
        self.debate_rules__motion_vetoes_enabled       = False
        # UI Options
        self.ui_options__show_novices                  = True


class WADLPreferences(PreferencesPreset):
    """ Example high school league setup """
    def __init__(self):
        self.name                                      = "WADL"
        self.show_in_list                              = True
        # Debate Rules= no replies; singular motions
        self.debate_rules__reply_scores_enabled        = False
        self.debate_rules__motion_vetoes_enabled       = False
        # Standings Rules
        self.standings__standings_missed_debates       = 0
        self.standings__team_standings_rule            = 'wadl'
        self.standings__speaker_standings_rule         = 'wadl'
        # Draws
        self.draw_rules__avoid_same_institution        = False
        self.draw_rules__avoid_team_history            = False
        self.draw_rules__draw_odd_bracket              = 'intermediate_bubble_up_down'
        self.draw_rules__draw_side_allocations         = 'balance'
        self.draw_rules__draw_pairing_method           = 'slide'
        self.draw_rules__draw_avoid_conflicts          = 'one_up_one_down'
        # Debate Rules
        self.debate_rules__substantive_speakers        = 3
        self.debate_rules__reply_scores_enabled        = True
        self.debate_rules__motion_vetoes_enabled       = True
        # UI Options
        self.ui_options__show_novices                  = True
        self.ui_options__show_emoji                    = False
        self.ui_options__show_institutions             = False
        self.ui_options__show_speakers_in_draw         = False
        self.ui_options__public_motions_descending     = True
        self.ui_options__show_all_draws                = True
        # League Options
        self.league_options__enable_flagged_motions    = True
        self.league_options__enable_adj_notes          = True
        self.league_options__enable_venue_groups       = True
        self.league_options__enable_venue_times        = True
        self.league_options__enable_venue_overlaps     = True
        self.league_options__share_adjs                = True
        self.league_options__duplicate_adjs            = True
        self.league_options__public_divisions          = True
        self.league_options__show_avg_margin           = True
        self.league_options__enable_divisions          = True
        self.league_options__enable_postponements      = True
        self.league_options__enable_forfeits           = True
        self.league_options__enable_division_motions   = True
        self.league_options__team_points_rule          = 'wadl'

